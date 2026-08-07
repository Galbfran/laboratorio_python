def main() -> None:
    print("Hello from functions!")
    print(saludar("Franco"))
    print(describir("pan", "leche", "huevos"))


def saludar(nombre: str, saludo: str = "Hola") -> str:
    return f"{saludo}, {nombre}"

def describir(*items: str) -> None:
    print(f"Recibí {len(items)} items")
    for item in items:
        print(f"- {item}")
