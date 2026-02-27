"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from ..utils import utils

from ..layouts.baselayout import base_layout
from ..state.state import State
from ..navigation.routes import Routes


@rx.page(Routes.INDEX.value,
        title=utils.index_title,
        description=utils.index_description,
        meta=utils.index_meta)
def index() :
    # Welcome Page (Index)
    return base_layout(
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
