import reflex as rx

from .pages.index import index
from .pages.auth.register import form_register
from .pages.auth.login import form_login    
from .api.api import fastapi_app



app = rx.App(api_transformer=fastapi_app)
app.add_page(index)
app.add_page(form_register) 
app.add_page(form_login) 



