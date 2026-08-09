from datetime import date
import json
from pathlib import Path

from gastos.domain.errores import ArchivoCorruptoError
from gastos.domain.gasto import Categoria, Gasto


class RepositorioJson:
    def __init__(self, ruta: Path) -> None:
        self._ruta = ruta
    def cargar(self) -> list[Gasto]:
        if not self._ruta.exists():
            return []

        try:
            contenido = json.loads(self._ruta.read_text())
        except json.JSONDecodeError as e:
            raise ArchivoCorruptoError(f"El archivo {self._ruta} tiene JSON inválido") from e

        return [
            Gasto(
                monto=item["monto"],
                categoria=Categoria(item["categoria"]),
                fecha=date.fromisoformat(item["fecha"]),
                descripcion=item["descripcion"],
            )
            for item in contenido
        ]
    
    def guardar(self, gastos: list[Gasto]) -> None:
        datos = [
            {
                "monto": gasto.monto,
                "categoria": gasto.categoria.value,
                "fecha": gasto.fecha.isoformat(),
                "descripcion": gasto.descripcion,
            }
            for gasto in gastos
        ]

        ruta_temporal = self._ruta.with_suffix(".tmp")
        ruta_temporal.write_text(json.dumps(datos, indent=2))
        ruta_temporal.replace(self._ruta)