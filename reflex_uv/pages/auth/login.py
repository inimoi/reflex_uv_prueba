import reflex as rx

from ...api.auth import Login
from ...api.api import login

class FormState(rx.State):
    form_data: dict = {}
    

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        datos_log = Login(
            email=form_data.get("email"),
            password=form_data.get("password")
        )
        respuesta = await login(datos_log)    
        print("Function response:", respuesta)

@rx.page("/auth/login")
def form_login():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(placeholder="Email", name="email", type="email"),
                rx.input(placeholder="Password", name="password", type="password"),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        
    )