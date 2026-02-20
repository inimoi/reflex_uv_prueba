import reflex as rx
from ...api.api import register
from ...api.auth import Register


class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        usuario:Register = Register(
            email=form_data.get("email"),
            password=form_data.get("password"),
            name=form_data.get("name")
        )
        respuesta = await register(usuario)

        print("Function response:", respuesta)  


@rx.page("/auth/register")
def form_register():
    return rx.center(
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Name", name="name"),
                    rx.input(placeholder="Email", name="email", type="email"),
                    rx.input(placeholder="Password", name="password", type="password"),                   
                    rx.button("Submit", type="submit"),
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),                  
        ),
        style={"padding": "2rem"},
        padding_top="8rem",
    )