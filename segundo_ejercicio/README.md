# Python — Colecciones (list, dict, set, tuple)

> Referencia rápida de la Clase 2. Comparado con Dart, que es de donde venís.

---

## 1. Las cuatro colecciones, de un vistazo

| Python  | Dart                        | Mutable | Ordenado       | Duplicados    |
| ------- | --------------------------- | ------- | -------------- | ------------- |
| `list`  | `List`                      | Sí      | Sí             | Sí            |
| `tuple` | — (más cercano a un record) | **No**  | Sí             | Sí            |
| `dict`  | `Map`                       | Sí      | Sí (desde 3.7) | claves únicas |
| `set`   | `Set`                       | Sí      | No             | No            |

**La que no tiene equivalente directo en Dart es `tuple`.** No es "una lista inmutable" nada más — está pensada para agrupar valores heterogéneos de tamaño fijo, más parecida a un record `(int, String)` que a un `List<T>`.

---

## 2. `list`

```python
numeros: list[int] = [1, 2, 3]

numeros.append(4)          # agrega al final
numeros.insert(0, 0)       # inserta en posición
numeros.remove(2)          # saca el primer 2 que encuentra (por valor)
numeros.pop()               # saca y devuelve el último
numeros[0]                  # acceso por índice, igual que Dart
numeros[-1]                  # último elemento — esto NO existe en Dart así de directo
numeros[1:3]                 # slicing: sublista desde índice 1 hasta 3 (exclusivo)
len(numeros)                 # tamaño

3 in numeros                 # pertenencia — devuelve bool
```

**Slicing** es algo que en Dart hacés con `.sublist()`, acá es sintaxis del lenguaje:

```python
lista = [0, 1, 2, 3, 4, 5]
lista[1:4]     # [1, 2, 3]
lista[:3]      # [0, 1, 2]  — desde el principio
lista[3:]      # [3, 4, 5]  — hasta el final
lista[::-1]    # [5, 4, 3, 2, 1, 0]  — invertida
```

---

## 3. `tuple`

Inmutable. Se define con `()` en vez de `[]`.

```python
punto: tuple[int, int] = (3, 4)
x, y = punto              # desestructuración — como records en Dart moderno

punto[0]                  # acceso por índice, sí se puede
punto[0] = 10              # ❌ TypeError — no se puede mutar
```

**Trampa de sintaxis:** una tupla de un solo elemento necesita coma, si no Python la interpreta como paréntesis normal:

```python
no_es_tupla = (5)       # esto es un int, no una tupla
si_es_tupla = (5,)      # esto sí es una tupla de un elemento
```

**Cuándo usarla en vez de `list`:** cuando el conjunto de valores es fijo y no vas a agregar/sacar nada — por ejemplo, devolver dos valores desde una función:

```python
def dividir(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b   # cociente y resto

cociente, resto = dividir(17, 5)
```

---

## 4. `dict`

```python
persona: dict[str, str] = {"nombre": "Franco", "ciudad": "Buenos Aires"}

persona["nombre"]                    # acceso — KeyError si no existe
persona.get("edad")                  # None si no existe, no explota
persona.get("edad", "N/A")           # "N/A" si no existe — default explícito
persona["edad"] = 30                 # crea o actualiza, no hay diferencia de sintaxis

"nombre" in persona                  # pertenencia — chequea CLAVES, no valores
del persona["ciudad"]                # eliminar una clave

persona.keys()                       # todas las claves
persona.values()                     # todos los valores
persona.items()                      # pares (clave, valor)

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

**La diferencia real con `Map` de Dart:** acceder con `[]` a una clave inexistente **tira excepción** (`KeyError`), no devuelve `null` como en Dart. Por eso `.get()` es tan usado — es tu forma de pedir "dame esto o un default" sin manejar try/except.

```python
persona["telefono"]                   # KeyError 💥
persona.get("telefono")               # None, sin excepción
persona.get("telefono", "sin dato")   # "sin dato", sin excepción
```

---

## 5. `set`

```python
categorias: set[str] = {"comida", "ocio", "comida"}   # el duplicado se descarta solo
# categorias == {"comida", "ocio"}

categorias.add("transporte")
categorias.discard("ocio")        # no falla si no existe
categorias.remove("ocio")         # KeyError si no existe

"comida" in categorias            # pertenencia — O(1), muy rápido

# operaciones de conjuntos, como en matemática:
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # unión       -> {1, 2, 3, 4}
a & b     # intersección -> {2, 3}
a - b     # diferencia   -> {1}
a ^ b     # diferencia simétrica -> {1, 4}
```

**Cuándo usarlo:** cuando te importa la pertenencia ("¿está esto acá?") y no el orden ni los duplicados. Mucho más rápido que buscar en una `list` cuando el volumen crece.

---

## 6. Elegir cuál usar

| Necesito...                                       | Uso     |
| ------------------------------------------------- | ------- |
| Orden, permitir repetidos, voy a modificar        | `list`  |
| Agrupar N valores fijos y heterogéneos, inmutable | `tuple` |
| Buscar por clave (nombre → valor)                 | `dict`  |
| Solo saber si algo "está" o no, sin duplicados    | `set`   |

---

## 7. Sobre `-> None` (repaso de una duda que surgió)

Python no tiene `void` como Dart. Una función sin `return` explícito **siempre devuelve `None`** — es un valor real, no una categoría especial.

```python
def imprimir_algo() -> None:
    print("hola")
    # sin return -> devuelve None de todas formas

x = imprimir_algo()
print(x)   # None
```

`-> None` es una anotación para el linter/lector humano: "esta función existe por sus efectos secundarios, no por lo que devuelve". En runtime no te impide nada — a diferencia de `void` en Dart, que sí es chequeado por el compilador.

---

## 8. Errores típicos con colecciones

| Error                                                            | Por qué pasa                                                       | Fix                                                                          |
| ---------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `KeyError` al leer un dict                                       | Usaste `[]` en vez de `.get()` para una clave que puede no existir | `dict.get(clave, default)`                                                   |
| Mutar una lista mientras la recorrés con `for`                   | Comportamiento indefinido/bugs sutiles                             | Iterá sobre una copia (`lista[:]`) o construí una lista nueva                |
| Confundir `(5)` con `(5,)`                                       | Falta la coma                                                      | Tupla de 1 elemento siempre lleva coma                                       |
| Pensar que `dict` no tiene orden                                 | Cambió en Python 3.7 — ahora preserva orden de inserción           | No es un problema real, pero no confíes en orden alfabético si no lo pediste |
| Usar `list` cuando la pertenencia (`in`) es lo único que importa | Rendimiento pobre en listas grandes                                | `set` — `in` es O(1) contra O(n) de la lista                                 |

---

## 9. Siguiente paso

Con esto resolvés la Kata 1 (ventas: total facturado, unidades por producto, producto más vendido). El próximo tema es **comprehensions** — la forma "pythonica" de construir estas mismas colecciones en una sola línea, en vez de con `for` + `append`.
