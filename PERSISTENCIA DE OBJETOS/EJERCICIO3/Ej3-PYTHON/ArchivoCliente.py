import pickle
import os
from Cliente import Cliente

class ArchivoCliente:
    def __init__(self, nombre_archivo):
        self.__nomA = nombre_archivo

    def crearArchivo(self):
        with open(self.__nomA, 'wb') as f:
            pickle.dump([], f)

    def guardaCliente(self, cliente):
        lista = self.__leer_lista()
        lista.append(cliente)
        self.__escribir_lista(lista)

    def buscarCliente(self, id):
        lista = self.__leer_lista()
        for c in lista:
            if c.get_id() == id:
                return c
        return None

    def buscarCelular(self, numero):
        lista = self.__leer_lista()
        for c in lista:
            if c.get_telefono() == numero:
                return c
        return None

    def __leer_lista(self):
        if os.path.exists(self.__nomA):
            with open(self.__nomA, 'rb') as f:
                return pickle.load(f)
        return []

    def __escribir_lista(self, lista):
        with open(self.__nomA, 'wb') as f:
            pickle.dump(lista, f)