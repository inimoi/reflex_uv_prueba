import reflex as rx
from ..pages.auth.login import LoginState
from ..navigation.routes import Routes
from ..styles.colors import Color, TextColor
from ..styles.size import Size
from ..styles.fonts import Font, FontWeight

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text, 
            size="3", 
            weight="medium",
            color=TextColor.HEADER.value,
            transition="all 0.2s ease-in-out",
            _hover={
                "color": Color.PRIMARY.value,
                "transform": "translateY(-1px)",
            },
        ),
        href=url,
        text_decoration="none",
    )

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.flex(
                # Logo Section
                rx.hstack(
                    rx.box(
                        rx.image(
                            src="/logo.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        padding="2px",
                        background=f"linear-gradient(45deg, {Color.PRIMARY.value}, {Color.SECONDARY.value})",
                        border_radius="10px",
                    ),
                    rx.text(
                        "ReflexUV",
                        size="6",
                        weight="bold",
                        color=TextColor.HEADER.value,
                        font_family=Font.LOGO.value,
                        letter_spacing="-0.02em",
                    ),
                    align_items="center",
                    spacing="3",
                    cursor="pointer",
                    on_click=rx.redirect(Routes.INDEX.value),
                ),
                
                # Links Section
                rx.hstack(
                    navbar_link("Inicio", Routes.INDEX.value),
                    navbar_link("Explorar", "/#"),
                    navbar_link("Precios", "/#"),
                    navbar_link("Dashboard", Routes.AUTORIZADO.value),
                    spacing="6",
                    align_items="center",
                ),
                
                # Auth Section
                rx.cond(
                    LoginState.logged_in,
                    rx.hstack(
                        rx.text(f"Hola, {LoginState.usuario}", size="2", color=TextColor.BODY.value),
                        rx.button(
                            "Salir",
                            variant="surface",
                            size="2",
                            color_scheme="ruby",
                            on_click=LoginState.logout,
                        ),
                        spacing="4",
                        align_items="center",
                    ),
                    rx.hstack(
                        rx.button(
                            "Log In",
                            variant="ghost",
                            size="2",
                            color=TextColor.HEADER.value,
                            _hover={"background": f"{Color.PRIMARY.value}11"},
                            on_click=rx.redirect(Routes.LOGIN.value),
                        ),
                        rx.button(
                            "Register",
                            variant="surface",
                            size="2",
                            background=Color.PRIMARY.value,
                            color=Color.BACKGROUND.value,
                            _hover={"background": Color.SECONDARY.value},
                            on_click=rx.redirect(Routes.REGISTER.value),
                        ),
                        spacing="4",
                        align_items="center",
                    ),
                ),
                justify="between",
                align_items="center",
                width="100%",
                max_width="1200px",
                margin_x="auto",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(src="/logo.jpg", width="2em", height="auto", border_radius="25%"),
                    rx.text("ReflexUV", size="5", weight="bold", font_family=Font.LOGO.value),
                    spacing="2",
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=24, color=TextColor.HEADER.value)
                    ),
                    rx.menu.content(
                        rx.menu.item("Inicio", on_click=rx.redirect(Routes.INDEX.value)),
                        rx.menu.item("Dashboard", on_click=rx.redirect(Routes.AUTORIZADO.value)),
                        rx.menu.separator(),
                        rx.cond(
                            LoginState.logged_in,
                            rx.menu.item("Cerrar Sesión", color="red", on_click=LoginState.logout),
                            rx.menu.item("Iniciar Sesión", on_click=rx.redirect(Routes.LOGIN.value)),
                        ),
                    ),
                ),
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        # Glassmorphism effect
        background="rgba(15, 23, 42, 0.8)",
        backdrop_filter="blur(12px)",
        border_bottom=f"1px solid {Color.PRIMARY.value}22",
        padding_y="0.75rem",
        padding_x="1.5rem",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
    )