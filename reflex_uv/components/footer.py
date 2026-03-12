import reflex as rx
from ..styles.colors import Color, TextColor
from ..styles.size import Size
from ..styles.fonts import Font, FontWeight

def footer_link(text: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="3"),
        href=href,
        color=TextColor.BODY.value,
        transition="all 0.3s ease",
        _hover={
            "color": Color.PRIMARY.value,
            "transform": "translateX(5px)",
        },
    )

def footer_column(title: str, links: list[tuple[str, str]]) -> rx.Component:
    return rx.vstack(
        rx.text(
            title,
            size="4",
            weight="bold",
            color=TextColor.HEADER.value,
            font_family=Font.TITLE.value,
            margin_bottom=Size.SMALL.value,
        ),
        rx.vstack(
            *[footer_link(text, href) for text, href in links],
            align_items="start",
            spacing="2",
        ),
        align_items="start",
        spacing="3",
    )

def social_icon(icon_name: str, href: str) -> rx.Component:
    return rx.link(
        rx.center(
            rx.icon(icon_name, size=20),
            width="40px",
            height="40px",
            border_radius="full",
            background=Color.CONTENT.value,
            color=TextColor.HEADER.value,
            transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
            _hover={
                "background": Color.PRIMARY.value,
                "color": Color.BACKGROUND.value,
                "transform": "translateY(-3px)",
                "box_shadow": f"0 10px 15px -3px {Color.PRIMARY.value}44",
            },
        ),
        href=href,
    )

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.divider(border_color=f"{Color.PRIMARY.value}22"),
            rx.flex(
                # Brand Section
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.image(
                                src="/logo.jpg",
                                width="32px",
                                height="32px",
                                border_radius="8px",
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
                        ),
                        align_items="center",
                        spacing="3",
                    ),
                    rx.text(
                        "Construyendo el futuro de la web con Python y Reflex. Diseño premium para aplicaciones modernas.",
                        size="2",
                        color=TextColor.BODY.value,
                        max_width="300px",
                        margin_top=Size.SMALL.value,
                    ),
                    rx.hstack(
                        social_icon("instagram", "#"),
                        social_icon("twitter", "#"),
                        social_icon("github", "#"),
                        social_icon("linkedin", "#"),
                        spacing="3",
                        margin_top=Size.DEFAULT.value,
                    ),
                    align_items="start",
                    flex="1",
                ),
                
                # Links Sections
                rx.flex(
                    footer_column(
                        "Producto",
                        [
                            ("Características", "#"),
                            ("Componentes", "#"),
                            ("Ejemplos", "#"),
                            ("Precios", "#"),
                        ]
                    ),
                    footer_column(
                        "Comunidad",
                        [
                            ("Github", "#"),
                            ("Discord", "#"),
                            ("Documentación", "#"),
                            ("Blog", "#"),
                        ]
                    ),
                    footer_column(
                        "Legal",
                        [
                            ("Privacidad", "#"),
                            ("Términos", "#"),
                            ("Cookies", "#"),
                        ]
                    ),
                    spacing="8",
                    flex_direction=["column", "row", "row"],
                    flex="2",
                    justify="between",
                    padding_top=["2em", "0", "0"],
                ),
                
                width="100%",
                flex_direction=["column", "column", "row"],
                justify="between",
                spacing="9",
                padding_y=Size.VERY_BIG.value,
            ),
            
            rx.divider(border_color=f"{Color.PRIMARY.value}11"),
            
            # Bottom Bar
            rx.flex(
                rx.text(
                    "© 2026 ReflexUV. Hecho con ❤️ por Antigravity.",
                    size="1",
                    color=TextColor.FOOTER.value,
                ),
                rx.hstack(
                    rx.text("Status: Online", size="1", color="#10B981"),
                    rx.box(width="8px", height="8px", border_radius="full", background="#10B981"),
                    align_items="center",
                    spacing="2",
                ),
                width="100%",
                justify="between",
                padding_y=Size.DEFAULT.value,
            ),
            
            width="100%",
            max_width="1200px",
            margin_x="auto",
            padding_x=Size.DEFAULT.value,
        ),
        width="100%",
        background=Color.BACKGROUND.value,
        # Subtle top glow
        box_shadow=f"0 -1px 20px 0 {Color.PRIMARY.value}11",
    )