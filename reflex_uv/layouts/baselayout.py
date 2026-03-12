import reflex as rx
from ..components.navbar import navbar_buttons
from ..components.footer import footer
from ..styles.colors import Color

def base_layout(*args, **kwargs) -> rx.Component:
    return rx.box(
        navbar_buttons(),
        rx.box(
            rx.vstack(
                *args,
                **kwargs,
                spacing="0",
                width="100%",
                align_items="center",
            ),
            width="100%",
            min_height="85vh",
        ),
        footer(),
        width="100%",
        background=Color.BACKGROUND.value,
        id="base-layout-root",
    )