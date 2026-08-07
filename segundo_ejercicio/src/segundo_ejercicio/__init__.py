def main() -> None:
    print("Hello from segundo-ejercicio!")


list = [1, 2, 3, 4, 5]

tuple = (1, 2, 3, 4, 5)

dict = {"a": 1, "b": 2, "c": 3}

set = {1, 2, 3, 4, 5, 5, 5, 5}

for i in list:
    print("Número en la lista: " + str(i))

for i in tuple:
    print("Número en la tupla: " + str(i))

for key, value in dict.items():
    print("Clave: " + str(key) + ", Valor: " + str(value))

for i in set:
    print("Número en el conjunto: " + str(i))