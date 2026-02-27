
import reflex as rx
from ..layouts.protected.protected_routes import protected_page
from ..pages.auth.login import FormState
from ..layouts.baselayout import base_layout
from ..utils import utils

@rx.page("/autorizado/", 
        title=utils.autorizado_title,
        description=utils.autorizado_description,
        meta=utils.autorizado_meta,
        on_load=FormState.validate_token_app)
def autorizado() :
    # Welcome Page (Index)
    return protected_page(
        base_layout(
            rx.vstack(
                rx.heading("Dashboard"),
                # Tu contenido aquí
            ),
        )
    )

