import reflex as rx
from .colors import Color, TextColor
from .size import Size
from .fonts import Font, FontWeight





STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    # "/css/styles.css"
]


#Styles


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.BODY.value
)
