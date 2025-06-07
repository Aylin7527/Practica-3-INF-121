from typing import Generic, TypeVar, List
T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.__contenido: List[T] = []

    def guardar(self, valor: T):
        self.__contenido.append(valor)

    def obtener(self, i: int) -> T :
        if i < 0 or i >= len(self.__contenido):
            print("Índice fuera de rango.")
            return None
        else:
            return self.__contenido[i]
print("--- Primera Instancia de Caja ---")
caja_texto = Caja[str]()
caja_texto.guardar("Hola, como estas?")
print(caja_texto.obtener(0))
print("--- Segunda Instancia de Caja ---")
caja_numero = Caja[int]()
caja_numero.guardar(12345)
print(caja_numero.obtener(0))