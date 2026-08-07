def main() -> None:
    print(f"Valor total de los libros: ${get_total_price(libros)}")
    print(f"Libros sin stock: {get_books_not_stock(libros)}")
    print(f"Autores de los libros: {get_authos(libros)}")
    print(f"Libros de Robert Martin: {get_books_by_author(libros, 'Robert Martin')}")
    print("Fin del programa.")

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

def get_books_not_stock(books: list[dict[str, str | int]]) -> list[str]:
    not_in_stock = []
    for book in books:
        if isinstance(book["stock"], int) and book["stock"] == 0:
            not_in_stock.append(book["titulo"])
    return not_in_stock

def get_authos(books: list[dict[str, str| int]]) -> set[str]:
    books_by_author = set(book["autor"] for book in books if isinstance(book["autor"], str))
   
    return books_by_author

def get_books_by_author(books: list[dict[str, str| int]], author: str) -> list[str]:
    books_by_author = []
    for book in books:
        if isinstance(book["autor"], str) and book["autor"] == author:
            books_by_author.append(book["titulo"])
    return books_by_author