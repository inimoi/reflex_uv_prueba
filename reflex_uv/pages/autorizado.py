
import reflex as rx
from ..layouts.protected.protected_routes import protected_page
from ..pages.auth.login import LoginState
from ..layouts.baselayout import base_layout
from ..utils import utils
from ..navigation.routes import Routes

@rx.page(Routes.AUTORIZADO.value, 
        title=utils.autorizado_title,
        description=utils.autorizado_description,
        meta=utils.autorizado_meta,
        on_load=LoginState.validate_token_app)
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
