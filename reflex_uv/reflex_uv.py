import reflex as rx

from .pages.index import index
from .pages.autorizado import autorizado
from .pages.auth.register import form_register
from .pages.auth.login import form_login   
from .pages.contacto import contacto
from .pages.upload import upload_page
from .api.api import fastapi_app



from .styles.styles import BASE_STYLE, STYLESHEETS

app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLESHEETS,
    api_transformer=fastapi_app
)
# No es necesario add_page si se usa el decorador @rx.page en los archivos de página.



