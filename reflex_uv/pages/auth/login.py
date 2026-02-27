import reflex as rx
from fastapi.security import HTTPAuthorizationCredentials

from ...api.auth import Login
from ...api.api import login
from ...api.api import validate_token_endpoint
from ...utils import utils
from ...navigation.routes import Routes



class FormState(rx.State):
    form_data: dict = {}
    logged_in: bool = False
    token_local_storage: str | None = rx.LocalStorage( name="token_local_storage", sync=True)
    user_data: dict = {}
    is_valid: bool = False
    error_message: str = ""
    usuario: str = ""

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

        datos_log = Login(
            email=form_data.get("email"),
            password=form_data.get("password")
        )
        respuesta = await login(datos_log)  
        if respuesta:
            self.logged_in = True
            self.usuario = respuesta["user"]["email"]
            
        token: str = respuesta.get("access_token", "")
        
        self.token_local_storage = token
        return rx.redirect("/")  

    ##### Tenemos que poera aqui los métodos de validación del token para que se actualice el estado de autenticación en toda la app #####
    async def validate_token_app(self):
        """Valida el token llamando al endpoint"""
        if not self.token_local_storage:
            self.is_valid = False
            self.error_message = "No se proporcionó token"
            return self.error_message
        credenciales = HTTPAuthorizationCredentials(scheme="Bearer", credentials=self.token_local_storage)
        try:
            result = await validate_token_endpoint(credentials=credenciales)
            self.is_valid = result["valid"]
            
            if not self.is_valid:
                self.error_message = "Token inválido"
        except Exception as e:
            self.is_valid = False
            self.error_message = str(e)       
        
    

        

@rx.page(Routes.LOGIN.value,
        title=utils.login_title,
        description=utils.login_description,
        meta=utils.login_meta)
def form_login():
    return rx.center(
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Email", name="email", type="email"),
                    rx.input(placeholder="Password", name="password", type="password"),
                    rx.button("Submit", type="submit"),
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
                ),
            
            ),
        padding_top="8rem",
        ),
        
       
