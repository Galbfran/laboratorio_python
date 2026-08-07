def main() -> None:
    print("Hello from primer-ejercicio!")

edad = 12
precio = 19.00
name = "Juan"
null = None
edadTexto = str(edad)

print("Hola, mi nombre es " + name + ", tengo " + str(edad) + " años y el precio es de $" + str(precio))
print("Hola, mi nombre es " + name + ", tengo " + edadTexto + " años y el precio es de $" + str(precio))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


if null is None:
    print("La variable 'null' es None.")
else: 
    print("La variable 'null' no es None.")

lista = [1, 2, 3, 4, 5]
for numero in lista:
    print("Número en la lista: " + str(numero))

for i , fruta in enumerate(["manzana", "banana", "cereza"]):
    print("Fruta " + str(i) + ": " + fruta)

def describir(status: str) -> str:
    match status:
        case "activo":
            return "El estado es activo."
        case "inactivo":
            return "El estado es inactivo."
        case _:
            return "El estado es: " + status