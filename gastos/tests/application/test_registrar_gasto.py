from datetime import date
from gastos.domain.errores import MontoInvalidoError
import pytest  # type: ignore

from gastos.application.use_cases.registrar_gasto import RegistrarGasto
from gastos.adapters.persistence.repositorio_en_memoria import RepositorioEnMemoria
from gastos.domain.gasto import Gasto, Categoria


def test_registrar_gasto_lo_guarda_en_el_repositorio():
    repositorio = RepositorioEnMemoria()
    caso_de_uso = RegistrarGasto(repositorio)
    gasto = Gasto(1500, Categoria.COMIDA, date.today(), "almuerzo")

    caso_de_uso.ejecutar(gasto)

    assert repositorio.cargar() == [gasto]

def test_registrar_gasto_preserva_los_gastos_existentes():
    repositorio = RepositorioEnMemoria()
    gasto_previo = Gasto(1000, Categoria.TRANSPORTE, date.today(), "colectivo")
    repositorio.guardar([gasto_previo])

    caso_de_uso = RegistrarGasto(repositorio)
    gasto_nuevo = Gasto(1500, Categoria.COMIDA, date.today(), "almuerzo")
    caso_de_uso.ejecutar(gasto_nuevo)

    assert repositorio.cargar() == [gasto_previo, gasto_nuevo]

def test_no_se_puede_registrar_un_gasto_invalido():
    repositorio = RepositorioEnMemoria()
    caso_de_uso = RegistrarGasto(repositorio)

    with pytest.raises(MontoInvalidoError):
        gasto_invalido = Gasto(-100, Categoria.COMIDA, date.today())
        caso_de_uso.ejecutar(gasto_invalido)