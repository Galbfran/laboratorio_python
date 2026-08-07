# Python — Funciones

> Referencia rápida del Tema 4. Foco extendido en `*args` y `**kwargs`, que es donde más dudas suelen surgir viniendo de Dart/TS.

---

## 1. Lo que ya conocés (repaso corto)

```python
def saludar(nombre: str, saludo: str = "Hola") -> str:
    return f"{saludo}, {nombre}"

saludar("Franco")                    # "Hola, Franco" — usa el default
saludar("Franco", "Buenas")          # posicional
saludar("Franco", saludo="Buenas")   # keyword arg explícito
saludar(nombre="Franco")             # también podés nombrar el primero
```

Esto ya lo venís haciendo en tus funciones (`get_books_by_author(books, author)`, todas tipadas). No hay nada nuevo conceptualmente acá comparado con Dart — parámetros con default son parecidos a los `parametro = valor` opcionales de Dart.

**Diferencia real con Dart:** Python no tiene _function overloading_ (dos funciones con mismo nombre, distinta firma). `*args`, `**kwargs` y los defaults son, en gran parte, la forma que tiene Python de cubrir los casos donde en Dart usarías overloads.

---

## 2. `*args` — cantidad variable de argumentos posicionales

### Qué es

El `*` le dice a Python "juntá todos los argumentos posicionales sobrantes en una `tuple`". El nombre `args` es convención, no obligación — podría llamarse `*numeros`, `*valores`, lo que sea.

```python
def sumar(*numeros: int) -> int:
    return sum(numeros)

sumar(1, 2, 3)        # 6 — numeros = (1, 2, 3)
sumar(1, 2, 3, 4, 5)   # 15 — numeros = (1, 2, 3, 4, 5)
sumar()                 # 0 — numeros = ()
```

Adentro de la función, `numeros` **es una `tuple` normal** — podés iterarla, indexarla, todo lo que ya sabés de tuplas:

```python
def describir(*items: str) -> None:
    print(f"Recibí {len(items)} items")
    for item in items:
        print(f"- {item}")

describir("pan", "leche", "huevos")
# Recibí 3 items
# - pan
# - leche
# - huevos
```

### Por qué existe — el problema que resuelve

Sin `*args`, si quisieras una función que sume "cualquier cantidad" de números, tendrías que recibir explícitamente una `list`:

```python
def sumar(numeros: list[int]) -> int:
    return sum(numeros)

sumar([1, 2, 3])   # tenés que armar la lista vos mismo, con corchetes
```

`*args` te deja llamarla de forma más natural, sin armar la colección a mano:

```python
sumar(1, 2, 3)   # más directo, sin corchetes
```

### Desempaquetar una lista existente en `*args`

Si ya tenés una `list`/`tuple` y querés pasarla a una función que espera `*args`, usás `*` también al llamarla:

```python
numeros = [1, 2, 3, 4]
sumar(*numeros)   # equivale a sumar(1, 2, 3, 4)
```

Este mismo `*` para "desempaquetar" es el mismo símbolo que para "empaquetar" — el contexto (definición vs. llamada) determina cuál de las dos cosas hace.

---

## 3. `**kwargs` — cantidad variable de argumentos con nombre

### Qué es

El `**` junta todos los _keyword arguments_ sobrantes en un `dict`. Es el equivalente más cercano que tenés en Dart a recibir un `Map<String, dynamic>` de parámetros nombrados dinámicos.

```python
def crear_config(**opciones: str) -> dict[str, str]:
    return opciones

crear_config(host="localhost", puerto="8080")
# {"host": "localhost", "puerto": "8080"}

crear_config()
# {}
```

Fijate la diferencia con `*args`: acá **tenés que nombrar** cada argumento al llamar. Esto no funciona:

```python
crear_config("localhost", "8080")   # ❌ TypeError — kwargs necesita nombres
```

### Ejemplo más real — construir algo con opciones flexibles

```python
def crear_libro(titulo: str, **detalles: str | int) -> dict[str, str | int]:
    libro = {"titulo": titulo}
    libro.update(detalles)
    return libro

crear_libro("Rayuela", autor="Julio Cortázar", precio=15000, stock=5)
# {"titulo": "Rayuela", "autor": "Julio Cortázar", "precio": 15000, "stock": 5}

crear_libro("El Aleph", autor="Jorge Luis Borges")
# {"titulo": "El Aleph", "autor": "Jorge Luis Borges"}  — sin precio ni stock, y no explota
```

Esto es útil cuando no sabés de antemano cuántos "campos opcionales" va a tener cada llamado — parecido a un `Map` de opciones opcional en Dart, pero integrado a la firma de la función en vez de recibir un parámetro `Map` explícito.

### Desempaquetar un dict existente en `**kwargs`

```python
datos = {"autor": "Julio Cortázar", "precio": 15000}
crear_libro("Rayuela", **datos)
# equivale a crear_libro("Rayuela", autor="Julio Cortázar", precio=15000)
```

---

## 4. Combinando todo — el orden importa

Cuando una función mezcla parámetros normales, `*args` y `**kwargs`, tienen que ir en este orden:

```python
def funcion(posicional, *args, con_default="valor", **kwargs):
    ...
```

1. Parámetros posicionales normales
2. `*args`
3. Parámetros con nombre y default (keyword-only después de `*args`)
4. `**kwargs`

```python
def registrar_evento(nombre: str, *tags: str, prioridad: str = "normal", **metadata: str) -> None:
    print(f"Evento: {nombre}")
    print(f"Tags: {tags}")
    print(f"Prioridad: {prioridad}")
    print(f"Metadata: {metadata}")

registrar_evento(
    "login_fallido",
    "seguridad", "auth",             # -> tags
    prioridad="alta",                  # -> con_default, nombrado
    ip="192.168.1.1", intentos=3,      # -> metadata
)
```

---

## 5. Dónde te los vas a encontrar en la práctica

- **`argparse`** (Tema 11 del roadmap): internamente usa este patrón para juntar argumentos de línea de comandos.
- **Decoradores** (más adelante, no es tema de este bloque): casi todo decorador genérico en Python usa `*args, **kwargs` para "pasar cualquier cosa" a la función que decora, sin importarle la firma exacta.
- **Constructores flexibles**: clases que aceptan configuración variable (muy común en librerías) — es el mismo patrón que `crear_config` de arriba.
- **Wrappers/adaptadores**: cuando envolvés una función de terceros y necesitás reenviarle "lo que sea" que te pasaron, sin conocer de antemano su firma completa.

---

## 6. Retorno múltiple — repaso corto

No es un tipo especial, es azúcar sintáctica sobre `tuple`:

```python
def dividir(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b   # esto ES una tuple, aunque no tenga paréntesis

cociente, resto = dividir(17, 5)   # desestructuración — cociente=3, resto=2
```

---

## 7. Errores/excepciones propias — preview del próximo tema

```python
class DivisionInvalidaError(Exception):
    """Se lanza cuando el divisor es cero."""

def dividir_seguro(a: float, b: float) -> float:
    if b == 0:
        raise DivisionInvalidaError(f"No se puede dividir {a} por cero")
    return a / b

try:
    resultado = dividir_seguro(10, 0)
except DivisionInvalidaError as e:
    print(f"Error: {e}")
else:
    print(resultado)
finally:
    print("Operación terminada")
```

Heredar de `Exception` es la forma estándar de definir errores de dominio propios — mismo concepto que vas a aplicar (ya aplicaste) en `errors.dart` del lado Flutter.

---

## 8. Resumen rápido

| Necesito... | Uso |
|---|---|V
| Cantidad fija de parámetros | Parámetros normales, con o sin default |
| Cantidad variable de argumentos **sin nombre** | `*args` (llega como `tuple`) |
| Cantidad variable de argumentos **con nombre** | `**kwargs` (llega como `dict`) |
| Devolver más de un valor | `tuple` como return type, desestructurando al llamar |
| Comunicar un error de negocio propio | Clase que hereda de `Exception` + `raise` |
