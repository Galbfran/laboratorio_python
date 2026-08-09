from gastos.domain.gasto import Gasto


class RepositorioEnMemoria:
    def __init__(self) -> None:
        self._gastos: list[Gasto] = []

    def cargar(self) -> list[Gasto]:
        return list(self._gastos)

    def guardar(self, gastos: list[Gasto]) -> None:
        self._gastos = list(gastos)