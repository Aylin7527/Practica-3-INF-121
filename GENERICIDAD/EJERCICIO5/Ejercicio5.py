from typing import Generic, TypeVar, List
T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.__elementos: List[T] = []

    def apilar(self, item: T):
        self.__elementos.append(item)

    def desapilar(self) -> T:
        if not self.__elementos:
            raise IndexError("La pila está vacía")
        return self.__elementos.pop()

    def mostrar(self):
        print("Pila:", self.__elementos)

print("--- Prueba con enteros ---")
pila_int = Pila[int]()
pila_int.apilar(1)
pila_int.apilar(2)
pila_int.apilar(3)
pila_int.mostrar()
print("Desapilado:", pila_int.desapilar())
print("**** Después del Desapilado ****")
pila_int.mostrar()

print("--- Prueba con cadenas ---")
pila_str = Pila[str]()
pila_str.apilar("a")
pila_str.apilar("b")
pila_str.apilar("c")
pila_str.mostrar()
print("Desapilado:", pila_str.desapilar())
print("**** Después del Desapilado ****")
pila_str.mostrar()

print("--- Prueba con flotantes ---")
pila_float = Pila[float]()
pila_float.apilar(1.1)
pila_float.apilar(2.2)
pila_float.apilar(3.3)
pila_float.mostrar()
print("Desapilado:", pila_float.desapilar())
print("**** Después del Desapilado ****")
pila_float.mostrar()