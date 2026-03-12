from enum import Enum

class Size(Enum):
    ZERO = "0"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    
    # Alias para compatibilidad
    PEQUE = "0.5em"
    MEDIANO = "0.8em"
    LARGO = "1.5em"
    GRANDE = "2em"
    MUY_GRANDE = "4em"
