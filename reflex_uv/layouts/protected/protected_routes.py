import reflex as rx
from ...pages.auth.login import FormState


def protected_page(content: rx.Component) -> rx.Component:
    """
    Componente que protege una página.
    Si no está autenticado, redirige a login.
    """


    return rx.cond(
        (FormState.logged_in) | (FormState.is_valid),
        content,
        rx.vstack(
            rx.text("No autenticado, redirigiendo..."),
            rx.link("Ir a Login", href="/auth/login"),
        )
    )