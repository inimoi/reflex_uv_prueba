import reflex as rx

from .pages.index import index
from .pages.autorizado import autorizado
from .pages.auth.register import form_register
from .pages.auth.login import form_login    
from .api.api import fastapi_app

style = {
    "background_image": "url('/background.png')",
    "background_size": "cover",
    "background_repeat": "no-repeat",
    "background_attachment": "fixed",
}


from .styles.styles import BASE_STYLE, STYLESHEETS

app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLESHEETS,
    api_transformer=fastapi_app
)
# No es necesario add_page si se usa el decorador @rx.page en los archivos de página.



