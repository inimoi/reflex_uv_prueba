import reflex as rx
from pydantic import ValidationError
from fastapi.security import HTTPAuthorizationCredentials

from ...api.auth import Login
from ...api.api import login, validate_token_endpoint, get_profile_endpoint
from ...utils import utils
from ...navigation.routes import Routes


class LoginState(rx.State):
    is_loading: bool = False
    error_message: str = ""
    logged_in: bool = False
    usuario: str = ""
    token_local_storage: str | None = rx.LocalStorage(name="token_local_storage", sync=True)
    user_data: dict = {}

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.is_loading = True
        self.error_message = ""
        
        try:
            datos_log = Login(
                email=form_data.get("email"),
                password=form_data.get("password")
            )
            
            respuesta = await login(datos_log)  
            
            if respuesta and "access_token" in respuesta:
                self.logged_in = True
                self.usuario = respuesta["user"]["email"]
                self.token_local_storage = respuesta.get("access_token")
                yield rx.toast.success("¡Bienvenido de nuevo!")
                yield rx.redirect("/")
            else:
                self.error_message = "Credenciales incorrectas"
                yield rx.toast.error(self.error_message)

        except ValidationError as e:
            error = e.errors()[0]
            self.error_message = f"Dato no válido: {error.get('msg', 'Error de formato')}"
            yield rx.toast.error(self.error_message)
            
        except Exception as e:
            self.error_message = "Error en el inicio de sesión. Verifica tus credenciales."
            yield rx.toast.error(self.error_message)
            
        finally:
            self.is_loading = False

    async def validate_token_app(self):
        """Valida el token llamando al endpoint y carga el perfil si es válido"""
        if not self.token_local_storage:
            self.logged_in = False
            return
            
        credenciales = HTTPAuthorizationCredentials(scheme="Bearer", credentials=self.token_local_storage)
        try:
            result = await validate_token_endpoint(credentials=credenciales)
            if result.get("valid"):
                self.logged_in = True
                await self.load_user_profile()
            else:
                self.logged_in = False
        except Exception:
            self.logged_in = False
    
    async def load_user_profile(self):
        """Recupera el perfil del usuario desde el endpoint `/auth/me`."""
        if not self.token_local_storage:
            return
        credenciales = HTTPAuthorizationCredentials(scheme="Bearer", credentials=self.token_local_storage)
        try:
            perfil = await get_profile_endpoint(credentials=credenciales)
            self.user_data = perfil
            self.usuario = perfil.get("email", "")
        except Exception:
            pass
    
    @rx.event
    def logout(self):
        """Cierra sesión y borra el estado/local storage"""
        self.logged_in = False
        self.token_local_storage = None
        self.user_data = {}
        yield rx.toast.info("Sesión cerrada")
        yield rx.redirect(Routes.LOGIN.value)

    async def redirect_if_logged_in(self):
        """Redirige a index si el usuario ya está autenticado."""
        await self.validate_token_app()
        if self.logged_in:
            return rx.redirect(Routes.INDEX.value)


@rx.page(Routes.LOGIN.value,
        title=utils.login_title,
        description=utils.login_description,
        meta=utils.login_meta,
        on_load=LoginState.redirect_if_logged_in)
def form_login():
    return rx.center(
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.heading("Iniciar Sesión", size="6", margin_bottom="1rem"),
                    rx.input(placeholder="Email", name="email", type="email", required=True, width="100%"),
                    rx.input(placeholder="Password", name="password", type="password", required=True, width="100%"),
                    rx.button(
                        "Entrar", 
                        type="submit", 
                        width="100%",
                        loading=LoginState.is_loading,
                        color_scheme="blue",
                    ),
                    spacing="4",
                    width="100%",
                ),
                on_submit=LoginState.handle_submit,
                width="100%",
            ),
            rx.cond(
                LoginState.error_message != "",
                rx.text(LoginState.error_message, color="red", size="2"),
            ),
            rx.link("¿No tienes cuenta? Regístrate", href="/auth/register", size="2"),
            width="100%",
            max_width="400px",
            padding="2rem",
            background="rgba(255,255,255,0.05)",
            border_radius="1rem",
            box_shadow="lg",
        ),
        padding_top="8rem",
        width="100%",
    )
