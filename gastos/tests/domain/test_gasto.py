import pytest  # type: ignore
from datetime import date

from gastos.domain.gasto import Gasto, Categoria
from gastos.domain.errores import MontoInvalidoError


def test_crear_gasto_valido():
    gasto = Gasto(monto=100.0, categoria=Categoria.COMIDA, fecha=date.today(), descripcion="Almuerzo")
    assert gasto.monto == 100.0
    assert gasto.categoria == Categoria.COMIDA
    assert gasto.fecha == date.today()
    assert gasto.descripcion == "Almuerzo"

def test_monto_negativo_lanza_error():
    with pytest.raises(MontoInvalidoError):
        Gasto(monto=-100.0, categoria=Categoria.COMIDA, fecha=date.today(), descripcion="Almuerzo")
