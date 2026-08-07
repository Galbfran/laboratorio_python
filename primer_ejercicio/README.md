# Python — Tipos básicos y flujo de control

> Referencia rápida de la Clase 1. Pensada para vos que venís de Dart/TS — marco las diferencias que importan, no repito lo obvio.

---

## 1. Tipos básicos

| Tipo    | Ejemplo             | Equivalente en Dart                        |
| ------- | ------------------- | ------------------------------------------ |
| `int`   | `edad = 17`         | `int`                                      |
| `float` | `precio = 19.99`    | `double`                                   |
| `str`   | `nombre = "Franco"` | `String`                                   |
| `bool`  | `activo = True`     | `bool` (ojo: `True`/`False` con mayúscula) |
| `None`  | `valor = None`      | `null`                                     |

**Diferencia clave:** Python es de **tipado dinámico**. Podés escribir `x = 5` y después `x = "hola"` sin que nada te frene en runtime. Los _type hints_ (`x: int = 5`) son opcionales y no los chequea el intérprete — los chequea Ruff/mypy como herramienta externa. En Dart el compilador te para; en Python el linter te avisa, pero el código igual corre.

```python
edad: int = 17          # anotación de tipo — documentación + ayuda al linter
nombre: str = "Franco"
precio: float = 1500.0
activo: bool = True
sin_valor: None = None
```

### Conversión de tipos

```python
int("42")       # 42
str(42)         # "42"
float("3.14")   # 3.14
int(3.9)        # 3  (trunca, no redondea)
```

---

## 2. Operadores que cambian de sintaxis

| Operación                | Python             | Dart           |
| ------------------------ | ------------------ | -------------- |
| Igualdad                 | `==`               | `==`           |
| Identidad (mismo objeto) | `is`               | `identical()`  |
| Negación                 | `not x`            | `!x`           |
| AND / OR lógico          | `and` / `or`       | `&&` / `\|\|`  |
| Módulo                   | `%`                | `%`            |
| División entera          | `//`               | `~/`           |
| Potencia                 | `**`               | `Math.pow()`   |
| Ternario                 | `x if cond else y` | `cond ? x : y` |

**Trampa típica:** comparar con `None` siempre con `is`, nunca con `==`:

```python
if valor is None:      # ✅ correcto
    ...
if valor == None:       # ❌ funciona pero no es idiomático — Ruff te lo marca
    ...
```

---

## 3. `if` / `elif` / `else`

No hay `{}`. La indentación **es** el bloque. Usá 4 espacios (Ruff lo fuerza).

```python
edad = 17

if edad < 18:
    categoria = "menor"
elif edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(categoria)
```

Condiciones "truthy/falsy" (más permisivo que Dart, que exige `bool` explícito):

```python
if lista:        # True si la lista NO está vacía
    ...
if not lista:     # True si está vacía
    ...
if texto:         # True si el string no es ""
    ...
```

> ⚠️ Esto es cómodo pero puede esconder bugs. Si el linter (`SIM` en Ruff) te sugiere simplificar, hacele caso — pero no abuses del truthy-check cuando la intención es "es `None`" (ahí usá `is None`, no `if not x`).

---

## 4. `for` — siempre for-each

No existe `for(int i = 0; i < n; i++)`. Solo iterás sobre algo iterable.

```python
frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)

# con índice, cuando lo necesitás:
for i, fruta in enumerate(frutas):
    print(i, fruta)

# rango numérico:
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):  # inicio, fin (exclusivo), paso -> 2,4,6,8
    print(i)
```

`enumerate()` es el equivalente a lo que en Dart harías con `.asMap().entries` — pero mucho más directo.

---

## 5. `while`

Igual que en Dart, sin sorpresas:

```python
intentos = 0
while intentos < 3:
    intentos += 1   # no existe intentos++ en Python
    print(intentos)
```

`break` y `continue` funcionan igual que en Dart.

---

## 6. `match` — el "switch" de Python (3.10+)

Más parecido a tu `switch` exhaustivo sobre `sealed class` en Dart que a un `switch` clásico de C.

```python
def describir(status: str) -> str:
    match status:
        case "pendiente":
            return "esperando"
        case "completado":
            return "listo"
        case "fallido" | "cancelado":     # varios valores en un case
            return "no llegó a destino"
        case _:                            # default — obligatorio si no cubrís todo
            return "desconocido"
```

`match` también puede desestructurar (esto no tiene equivalente directo en Dart hasta records/patterns recientes):

```python
punto = (3, 0)
match punto:
    case (0, 0):
        print("origen")
    case (x, 0):
        print(f"sobre el eje X, x={x}")
    case (0, y):
        print(f"sobre el eje Y, y={y}")
    case (x, y):
        print(f"punto genérico ({x}, {y})")
```

---

## 7. f-strings — interpolación de strings

Equivalente directo a `'texto $variable'` de Dart:

```python
nombre = "Franco"
edad = 30
print(f"{nombre} tiene {edad} años")
print(f"el doble es {edad * 2}")
```

---

## 8. Errores típicos al arrancar (para no pisar el palito)

| Error                                                | Por qué pasa                                                            | Fix                                              |
| ---------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------ |
| `IndentationError`                                   | Mezclaste tabs y espacios, o indentación inconsistente                  | Configurá el editor para usar 4 espacios siempre |
| Olvidar los `:` al final de `if`/`for`/`while`/`def` | Costumbre de otros lenguajes                                            | Siempre `if condicion:`                          |
| `x++`                                                | No existe en Python                                                     | `x += 1`                                         |
| Comparar con `== None`                               | No idiomático                                                           | `is None`                                        |
| Pensar que `if lista:` chequea `None`                | Chequea vacío, no `None` — una lista vacía y `None` dan `False` los dos | Sé explícito si la distinción importa            |

---

## 9. Siguiente paso

Con esto ya podés resolver el ejercicio de `saludo.py`. El próximo tema del roadmap es **colecciones** (`list`, `dict`, `set`, `tuple`) — ahí es donde Python empieza a mostrar músculo comparado con Dart.
