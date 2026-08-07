def main() -> None:
    print("Valor total de los libros: $" + str(get_total_price(libros)))
    print("Libros sin stock:" + str(get_books_not_stock(libros)))

libros = [
    {"titulo": "Clean Code", "autor": "Robert Martin", "precio": 25000, "stock": 3},
    {"titulo": "El Aleph", "autor": "Jorge Luis Borges", "precio": 12000, "stock": 0},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "precio": 15000, "stock": 5},
    {"titulo": "Clean Architecture", "autor": "Robert Martin", "precio": 28000, "stock": 2},
    {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "precio": 11000, "stock": 1},
]

def get_total_price(books: list[dict[str, str| int]]) -> float:
    total = 0.0
    for book in books:
        if isinstance(book["precio"], (int, float)) and isinstance(book["stock"], int):
            total += float(book["precio"]) * book["stock"]
        else:
            if not isinstance(book["precio"], (int, float)):
                print(f"El precio del libro '{book['titulo']}' no es un número válido.")
            elif not isinstance(book["stock"], int):
                print(f"El stock del libro '{book['titulo']}' no es un número válido.")
    return total

def get_books_not_stock(books: list[dict[str, str| int]]) -> list[str]:
    not_in_stock = []
    for book in books:
        if isinstance(book["stock"], int) and book["stock"] == 0:
            not_in_stock.append(book["titulo"])
        else:
            print(f"El libro '{book['titulo']}' no tiene stock disponible.")
    return not_in_stock