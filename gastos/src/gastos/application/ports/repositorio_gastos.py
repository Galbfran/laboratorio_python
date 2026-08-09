from typing import Protocol

from gastos.domain.gasto import Gasto

class RepositorioGastos(Protocol):
    def cargar(self) -> list[Gasto]:
        ...
    def guardar(self, gastos: list[Gasto]) -> None:
        ...

