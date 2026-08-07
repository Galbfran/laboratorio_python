from pathlib import Path
import json

ruta = Path("datos.json")
ruta.write_text(json.dumps({"clave": "valor"}))
datos = json.loads(ruta.read_text())

from dataclasses import dataclass
from enum import StrEnum

class Categoria(StrEnum):
    FICCION = "ficcion"
    TECNICO = "tecnico"

@dataclass(frozen=True, slots=True)
class Libro:
    titulo: str
    autor: str
    precio: float
    stock: int


def main() -> None:
    print(datos)
