import reflex as rx
from ..api.api import read_root


class State(rx.State):
    """The state of the app."""
    texto = "Hola desde el estado de la página"

    async def prueba(self):
        salida = await read_root()
        self.texto = salida["message"]
        

    async def registro_estado(self):
        self.texto = "Estado registrado correctamente"