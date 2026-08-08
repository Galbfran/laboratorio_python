class ErrorGasto(Exception):
    """Excepción base para errores relacionados con la creación de gastos."""


class MontoInvalidoError(ErrorGasto):
    """Se lanza cuando el monto de un gasto no es positivo."""