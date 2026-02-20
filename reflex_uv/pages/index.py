"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx



from ..state.state import State


@rx.page("/")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            
            rx.button("Prueba", on_click=State.prueba),
            rx.heading("¡Bienvenido a Reflex + FastAPI!", size="2"),
            rx.text(State.texto + " - Edita el archivo 'index.py' para personalizar esta página."),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
