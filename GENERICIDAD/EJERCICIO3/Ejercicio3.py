from typing import TypeVar, Generic, List
T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.__elementos: List[T] = []

    def agregar(self, item: T):
        self.__elementos.append(item)

    def buscar(self, i: int) -> T :
        if 0 <= i < len(self.__elementos):
            return self.__elementos[i]
        else:
            print("Índice fuera de rango.")
            return None

    def mostrar_todo(self):
        for elem in self.__elementos:
            print(elem)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor}"

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: Bs {self.precio}"

catalogo_libros = Catalogo[Libro]()
catalogo_libros.agregar(Libro("Nosotros En La Luna", "Alice Kellen"))
catalogo_libros.agregar(Libro("Harry Potter", "J.K. Rowling"))
print("--- Catálogo de Libros ---")
catalogo_libros.mostrar_todo()

catalogo_productos = Catalogo[Producto]()
catalogo_productos.agregar(Producto("Laptop", 5500))
catalogo_productos.agregar(Producto("Mouse", 80))
print("--- Catálogo de Productos ---")
catalogo_productos.mostrar_todo()