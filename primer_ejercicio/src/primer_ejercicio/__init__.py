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

edad = 17

if edad < 18:
    categoria = "menor"
elif edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(categoria)

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