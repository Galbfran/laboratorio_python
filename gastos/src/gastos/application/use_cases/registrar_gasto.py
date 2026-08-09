from gastos.application.ports.repositorio_gastos import RepositorioGastos
from gastos.domain.gasto import Gasto


class RegistrarGasto:
    def __init__(self, repositorio:RepositorioGastos)-> None:
        self._repositorio = repositorio

    def ejecutar(self, gasto: Gasto)-> None:
        gastos = self._repositorio.cargar()
        gastos.append(gasto)
        self._repositorio.guardar(gastos)