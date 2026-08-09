from gastos.domain.errores import ArchivoCorruptoError
import pytest # type: ignore
from datetime import date
from pathlib import Path

from gastos.domain.gasto import Gasto, Categoria
from gastos.adapters.persistence.repositorio_en_memoria import RepositorioEnMemoria
from gastos.adapters.persistence.repositorio_json import RepositorioJson


@pytest.fixture(params=["memoria", "json"])
def repositorio(request, tmp_path: Path):
    if request.param == "memoria":
        return RepositorioEnMemoria()
    return RepositorioJson(tmp_path / "gastos.json")


def test_repositorio_vacio_devuelve_lista_vacia(repositorio):
    assert repositorio.cargar() == []


def test_guardar_y_cargar_devuelve_los_mismos_gastos(repositorio):
    gastos = [Gasto(1500, Categoria.COMIDA, date.today(), "almuerzo")]
    repositorio.guardar(gastos)
    assert repositorio.cargar() == gastos

def test_json_corrupto_lanza_error(tmp_path: Path):   # ← esto es lo nuevo
    ruta = tmp_path / "gastos.json"
    ruta.write_text("esto no es json valido {{{")
    repositorio = RepositorioJson(ruta)
    with pytest.raises(ArchivoCorruptoError):
        repositorio.cargar()