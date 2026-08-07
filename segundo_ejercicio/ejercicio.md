# Ejercicio — Inventario de una librería

> Práctica de `list[dict]`. Solo `for` normal — nada de comprehensions todavía (eso es el próximo tema).

---

## Datos de partida

```python
libros = [
    {"titulo": "Clean Code", "autor": "Robert Martin", "precio": 25000, "stock": 3},
    {"titulo": "El Aleph", "autor": "Jorge Luis Borges", "precio": 12000, "stock": 0},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "precio": 15000, "stock": 5},
    {"titulo": "Clean Architecture", "autor": "Robert Martin", "precio": 28000, "stock": 2},
    {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "precio": 11000, "stock": 1},
]
```

Cada libro es un `dict[str, str | int]`. La colección completa es un `list[dict]` — el patrón "tabla" que se repite todo el tiempo en datos reales (JSON, respuestas de API, filas de una consulta).

---

## Consignas

### 1. Valor total del inventario

Sumá `precio * stock` de todos los libros.

### 2. Libros sin stock

Una `list` con los **títulos** (no los dict completos) de los libros con `stock == 0`.

### 3. Autores únicos

Un `set` con los nombres de autor, sin repetidos.

> Pensalo: ¿por qué `set` acá y no `list`, dado lo que vimos de rendimiento y de duplicados?

### 4. Diccionario de libros por autor

Un `dict[str, list[str]]` donde la clave es el autor y el valor es una lista de títulos de ese autor.

Resultado esperado:

```python
{
    "Robert Martin": ["Clean Code", "Clean Architecture"],
    "Jorge Luis Borges": ["El Aleph", "Ficciones"],
    "Julio Cortázar": ["Rayuela"],
}
```

> Pista: hay que chequear si la clave (autor) ya existe en el diccionario antes de agregarle un título — si no existe, se crea primero con una lista vacía.

### 5. Libro más caro

El **título** del libro con `precio` más alto.

> Pensalo: ¿cómo comparás mientras recorrés, sin ordenar toda la lista?

---

## Criterio de aceptación

- Solo `for`, `if`, acceso a `dict`/`list` — nada de comprehensions ni funciones mágicas de librería.
- Cada resultado en una variable con nombre descriptivo (nada de `list`, `dict`, `x`, `temp`).
- Resultados impresos con f-strings, prolijo.
- `uv run ruff check .` sale limpio.

---

## Conceptos que este ejercicio ejercita

| Consigna              | Qué practica                                                                                                   |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 1 — Valor total       | Acumulador con `for`, acceso a dos claves del mismo dict                                                       |
| 2 — Sin stock         | Filtro manual con `if` dentro del `for`, construcción de una `list` nueva                                      |
| 3 — Autores únicos    | `set.add()`, por qué el orden y los duplicados no importan acá                                                 |
| 4 — Agrupar por autor | Patrón "verificar si existe la clave, si no, inicializarla" — la base de lo que después resuelve `defaultdict` |
| 5 — Máximo manual     | Comparación acumulada sin `max()` — entender qué hace `max()` por debajo antes de usarlo                       |

---

## Siguiente paso

Una vez resuelto con `for`, el próximo tema (**comprehensions**) te va a mostrar cómo las consignas 1, 2 y 3 se resuelven en una sola línea. La consigna 4 es la más interesante de comparar: ahí vas a conocer `collections.defaultdict`, que existe específicamente para el patrón "crear la clave si no existe".
