import reflex as rx
from pydantic import ValidationError
from ...api.api import register
from ...api.auth import Register
from ...utils import utils
from ...navigation.routes import Routes

class RegisterState(rx.State):
    error_message: str = ""
    is_loading: bool = False

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.is_loading = True
        self.error_message = ""
        
        try:
            usuario: Register = Register(
                email=form_data.get("email"),
                password=form_data.get("password"),
                name=form_data.get("name")
            )
            # Validación mediante Pydantic al instanciar Register
            respuesta = await register(usuario)
            
            yield rx.toast.info("Registro completado con éxito")
            yield rx.redirect("/")
            
        except ValidationError as e:
            error = e.errors()[0]
            msg = error.get("msg", "Error de validación")
            # Personalizar mensajes
            if "at least 8 characters" in msg:
                msg = "La contraseña debe tener al menos 8 caracteres"
            elif "at least 1 uppercase" in msg:
                msg = "La contraseña debe tener al menos una mayúscula"
            
            self.error_message = f"Dato no válido: {msg}"
            yield rx.toast.error(self.error_message)
            
        except Exception as e:
            self.error_message = f"Error en el servidor: {str(e)}"
            yield rx.toast.error(self.error_message)
            
        finally:
            self.is_loading = False


@rx.page(Routes.REGISTER.value,
        title=utils.register_title,
        description=utils.register_description,
        meta=utils.register_meta)
def form_register():
    return rx.center(
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.heading("Registrarse", size="6", margin_bottom="1rem"),
                    rx.input(placeholder="Nombre completo", name="name", required=True, width="100%"),
                    rx.input(placeholder="Correo electrónico", name="email", type="email", required=True, width="100%"),
                    rx.input(placeholder="Contraseña", name="password", type="password", required=True, width="100%"),                   
                    rx.button(
                        "Crear cuenta", 
                        type="submit",
                        loading=RegisterState.is_loading,
                        width="100%",
                        color_scheme="blue",
                    ),
                    spacing="4",
                    width="100%",
                ),
                on_submit=RegisterState.handle_submit,
                width="100%",
            ),
            rx.cond(
                RegisterState.error_message != "",
                rx.text(RegisterState.error_message, color="red", size="2"),
            ),
            rx.link("¿Ya tienes cuenta? Inicia sesión", href="/auth/login", size="2"),
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