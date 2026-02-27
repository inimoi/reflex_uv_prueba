import reflex as rx

# Común a todas las páginas

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

#el previemw de la carga, debería ser una imegen
preview ="https://static.wikia.nocookie.net/linux/images/0/09/Images_%284%29vcncgn.jpg/revision/latest?cb=20160321213201&path-prefix=es"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
]

#Página index
index_title = "Página inicial"
index_description = "Es la página de incio de la aplicación Reflex UV"
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
    ]
index_meta.extend(_meta)

#Página Pruebas autorizacion
autorizado_title = "Pruebas autorizacion"
autorizado_description = "es la paǵina que hago de pruebas para la autorizació"
autorizado_meta = [
    {"name": "og:title", "content": autorizado_title},
    {"name": "og:description", "content": autorizado_description},
    ]
autorizado_meta.extend(_meta)

#Página Login
login_title = "Login"
login_description = "Esta es la página de Login"
login_meta = [
    {"name": "og:title", "content": login_title},
    {"name": "og:description", "content": login_description},
    ]
login_meta.extend(_meta)

#Página Registro
register_title = "Registro"
register_description = "Esta es la página para registrarnos"
register_meta = [
    {"name": "og:title", "content": register_title},
    {"name": "og:description", "content": register_description},
    ]
register_meta.extend(_meta)

