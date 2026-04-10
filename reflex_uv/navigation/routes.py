from enum import Enum

class Routes(Enum):
# Agrega tus rutas aquí
    INDEX = '/'
    AUTORIZADO = '/autorizado'
    LOGIN = '/auth/login'
    REGISTER = '/auth/register'
    CONTACTO = '/contacto'
    UPLOAD = '/upload'



