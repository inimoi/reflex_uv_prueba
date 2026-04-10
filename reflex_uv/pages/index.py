"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from ..utils import utils

from ..layouts.baselayout import base_layout
from ..state.state import State
from ..navigation.routes import Routes


from .auth.login import LoginState

@rx.page(Routes.INDEX.value,
        title=utils.index_title,
        description=utils.index_description,
        meta=utils.index_meta,
        on_load=LoginState.validate_token_app)
def index() :
    return base_layout(
        rx.center(
            rx.vstack(
                # Título principal con estilo moderno
                rx.heading(
                    "Grafis papelería, copistería",
                    size="9",
                    weight="bold",
                    background_image="linear-gradient(270deg, #3b82f6, #8b5cf6)",
                    background_clip="text",
                    style={"WebkitTextFillColor": "transparent", "Color": "transparent"},
                    text_align="center",
                    margin_bottom="0.5rem"
                ),
                
                # Subtítulo descriptivo
                rx.text(
                    "Tu papelería y copistería",
                    size="5",
                    color=rx.color("slate", 11),
                    text_align="center",
                    max_width="600px",
                    margin_bottom="3rem"
                ),
                
                # Botones de llamada a la acción (Call to Action)
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Empezar Ahora",
                            size="4",
                            variant="solid",
                            color_scheme="blue",
                            padding_x="2rem",
                            padding_y="1.5rem",
                            border_radius="full",
                            cursor="pointer",
                            box_shadow="0 4px 14px 0 rgba(0, 118, 255, 0.39)",
                            _hover={"transform": "translateY(-2px)", "box_shadow": "0 6px 20px rgba(0, 118, 255, 0.23)"},
                            transition="all 0.2s ease"
                        ),
                        href=Routes.LOGIN.value,
                        underline="none"
                    ),
                    rx.link(
                        rx.button(
                            "Contactar",
                            size="4",
                            variant="soft",
                            color_scheme="gray",
                            padding_x="2rem",
                            padding_y="1.5rem",
                            border_radius="full",
                            cursor="pointer",
                            _hover={"transform": "translateY(-2px)", "background_color": rx.color("slate", 4)},
                            transition="all 0.2s ease"
                        ),
                        href=Routes.CONTACTO.value,
                        underline="none"
                    ),
                    rx.link(
                        rx.button(
                            "Subir Fotos",
                            size="4",
                            variant="soft",
                            color_scheme="green",
                            padding_x="2rem",
                            padding_y="1.5rem",
                            border_radius="full",
                            cursor="pointer",
                            _hover={"transform": "translateY(-2px)", "background_color": rx.color("green", 4)},
                            transition="all 0.2s ease"
                        ),
                        href=Routes.UPLOAD.value,
                        underline="none"
                    ),
                    spacing="5",
                    justify="center"
                ),
                
                align_items="center",
                justify_content="center",
                padding="4rem 2rem",
                width="100%",
                min_height="80vh",
            ),
            width="100%",
        )
    )
