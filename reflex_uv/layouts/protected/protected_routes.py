import reflex as rx
from ...pages.auth.login import LoginState


def protected_page(content: rx.Component) -> rx.Component:
    """
    Componente que protege una página.
    Si no está autenticado, redirige a login.
    """


    return rx.cond(
        (LoginState.logged_in),
        content,
        rx.vstack(
            rx.text("No autenticado, redirigiendo..."),
            rx.link("Ir a Login", href="/auth/login"),
        )
    )