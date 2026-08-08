from dataclasses import dataclass
from datetime import date
from enum import StrEnum

from gastos.domain.errores import MontoInvalidoError

class Categoria(StrEnum):
    comida = "comida"
    transporte = "transporte"
    ocio = "ocio"
    servicios = "servicios"
    otros = "otros"

@dataclass(frozen=True, slots=True)
class Gasto:
    monto: float
    categoria: Categoria
    fecha: date
    descripcion: str = ""
def __post_init__(self) -> None:
    if self.monto <= 0:
        raise MontoInvalidoError(f"El monto debe ser positivo, recibí {self.monto}")