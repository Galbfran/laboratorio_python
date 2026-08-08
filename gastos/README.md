# Proyecto `gastos` — Arquitectura hexagonal en Python

> Gestor de gastos por consola. Mismo ejercicio del roadmap de Python, armado con `domain/application/adapters` desde el arranque en vez de la estructura simple sugerida originalmente.

---

## 0. Setup

```bash
uv init gastos
cd gastos
uv add --dev pytest ruff
uv python pin 3.12
```

---

## 1. Estructura de carpetas

```
gastos/
├── pyproject.toml
├── src/
│   └── gastos/
│       ├── domain/
│       │   ├── gasto.py           # entidad Gasto, Categoria
│       │   └── errores.py         # excepciones propias
│       ├── application/
│       │   ├── ports/
│       │   │   └── repositorio_gastos.py   # el Protocol
│       │   └── use_cases/
│       │       ├── registrar_gasto.py
│       │       ├── calcular_resumen.py
│       │       └── filtrar_gastos.py
│       ├── adapters/
│       │   ├── persistence/
│       │   │   ├── repositorio_json.py
│       │   │   └── repositorio_en_memoria.py
│       │   └── cli/
│       │       └── cli.py
│       └── main.py                # composition root
└── tests/
    ├── domain/
    ├── application/
    └── adapters/
```

---

## 2. Qué va en cada capa

### `domain/`

El núcleo. **No importa nada fuera de `domain/`** — ni `json`, ni `pathlib`, ni `argparse`. Python puro. Acá vive:

- `Gasto`: entidad inmutable (`@dataclass(frozen=True, slots=True)`), con validación de negocio (monto positivo).
- `Categoria`: enum de valores fijos.
- Excepciones propias de dominio.

### `application/ports/`

Los contratos. Un `Protocol` que define qué necesita el núcleo del mundo exterior — cargar y guardar gastos — sin decir cómo se implementa. Equivalente a `abstract interface class` en Dart o `interface` en TS, pero sin necesitar herencia explícita: cualquier clase con la forma correcta cumple el contrato (_structural typing_).

### `application/use_cases/`

La orquestación. Cada caso de uso coordina dominio + puerto, recibiendo sus dependencias por parámetro (constructor o función) en vez de importarlas directamente. Esto es lo que los hace testeables con un fake, sin tocar disco.

### `adapters/persistence/`

Las implementaciones concretas del puerto:

- `RepositorioJson`: archivo real, escritura atómica, manejo de JSON corrupto.
- `RepositorioEnMemoria`: estructura en memoria, para tests.

Ninguna hereda formalmente del `Protocol` — el type checker las valida por su forma, no por declaración.

### `adapters/cli/`

La interfaz de consola. Recibe argumentos, invoca casos de uso, imprime resultados. Sin lógica de negocio propia.

### `main.py`

Composition root. El único archivo que conoce las clases concretas (`RepositorioJson`, no el `Protocol`). Arma el grafo de dependencias e inyecta.

---

## 3. Requerimientos funcionales

### Dominio

- `Categoria`: comida, transporte, ocio, servicios, otros.
- `Gasto`: `monto`, `categoria`, `fecha`, `descripcion` (con default). Monto debe ser positivo, si no falla la creación.

### Casos de uso

- **Registrar un gasto** — valida con el dominio, guarda vía el puerto.
- **Calcular resumen** — total facturado, total por categoría, promedio mensual (`"2026-03" -> monto`), top N gastos más grandes.
- **Filtrar gastos** — por rango de fechas y/o categoría.

### Puerto (`Protocol`)

Mínimo: `cargar()` y `guardar(gastos)`.

### Adaptadores de persistencia

- `RepositorioJson`:
  - `date` no es serializable a JSON directo → convertir a ISO y de vuelta.
  - Archivo inexistente → lista vacía, no excepción.
  - JSON corrupto → excepción propia, con el error original encadenado (`raise ... from e`).
  - Escritura atómica: escribir a `.tmp` y luego `.replace()` al archivo real.
- `RepositorioEnMemoria`: mismo contrato, sin tocar disco — para tests.

### Adaptador CLI

Subcomandos con `argparse`:

```bash
gastos agregar --monto 1500 --categoria comida --desc "almuerzo"
gastos listar --categoria comida
gastos resumen --mes 2026-03
gastos exportar --formato csv --salida gastos.csv
```

---

## 4. Regla de aceptación central

Todos los tests de los casos de uso corren con `RepositorioEnMemoria` — nunca tocan disco. Y el mismo test de contrato (batería idéntica de aserciones) tiene que pasar contra **las dos** implementaciones del repositorio:

```python
def repositorio_contract_tests(nombre, factory):
    def test_guarda_y_recupera():
        repo = factory()
        # ...

    def test_lista_vacia_si_no_hay_datos():
        repo = factory()
        # ...

repositorio_contract_tests("JSON", lambda: RepositorioJson(...))
repositorio_contract_tests("EnMemoria", lambda: RepositorioEnMemoria())
```

Si ambos pasan con el mismo test, los adaptadores son verdaderamente intercambiables — la prueba real de que el puerto está bien definido.

---

## 5. Regla de dependencia (la que hay que respetar en cada PR mental)

```
adapters  →  application  →  domain
```

- `domain/` no importa nada.
- `application/` importa `domain/`.
- `adapters/` importa `application/`.
- Nadie importa un adapter concreto excepto `main.py`.

**Test rápido:** abrí cualquier archivo de `domain/`. Si tiene un `import` que no sea de otro archivo de `domain/`, está mal.

---

## 6. Diferencia clave vs. Dart/Node (para no confundirse)

| Concepto                           | Dart/Flutter                                | Node/TS                                 | Python (acá)                                                              |
| ---------------------------------- | ------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------- |
| Definir un puerto                  | `abstract interface class`                  | `interface`                             | `Protocol`                                                                |
| Implementar un puerto              | `implements` explícito                      | `implements` explícito                  | Duck typing — solo necesita la forma correcta                             |
| Forzar "domain no depende de nada" | Package separado sin `flutter` → no compila | Test de arquitectura (fitness function) | Test de arquitectura (fitness function) — no hay compilador que lo fuerce |
| Composition root                   | `AppContainer` (Dart plano)                 | `main.ts`                               | `main.py`                                                                 |

---

## 7. Orden sugerido de construcción

1. `domain/gasto.py` + `domain/errores.py` — y sus tests, sin nada más.
2. `application/ports/repositorio_gastos.py` — el `Protocol`, sin implementación todavía.
3. `adapters/persistence/repositorio_en_memoria.py` — el primer adaptador, el más simple.
4. `application/use_cases/registrar_gasto.py` — primer caso de uso, testeado con el repo en memoria.
5. Resto de casos de uso (`calcular_resumen`, `filtrar_gastos`).
6. `adapters/persistence/repositorio_json.py` — segundo adaptador, ahí se prueba el test de contrato.
7. `adapters/cli/cli.py` + `main.py` — se cierra el círculo.

Este orden es intencional: construir de adentro hacia afuera (dominio primero, adaptadores al final) es lo que en la práctica te obliga a mantener la regla de dependencia, porque cuando escribís `application/` todavía no existe ningún adaptador concreto al que "atajarte" por comodidad.
