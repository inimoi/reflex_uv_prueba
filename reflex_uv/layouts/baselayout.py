import reflex as rx

from ..components.navbar import navbar_buttons
from ..components.footer import footer

def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        navbar_buttons(),
        rx.fragment(
            *args,
            **kwargs,
        ),

        footer(),
        id='my-base-container',
        size="4",
    )