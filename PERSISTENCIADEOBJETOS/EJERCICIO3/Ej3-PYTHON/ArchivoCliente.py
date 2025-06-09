import json
import os
from Cliente import Cliente

class ArchivoCliente:
    def __init__(self, nomA):
        self.__nomA = nomA

    def crearArchivo(self):
        with open(self.__nomA, 'w') as f:
            json.dump([], f)

    def guardaCliente(self, cliente):
        lista = self.__leer_lista()
        lista.append(cliente.to_dict())
        self.__escribir_lista(lista)

    def buscarCliente(self, id):
        lista = self.__leer_lista()
        for c in lista:
            if c["id"] == id:
                return Cliente.from_dict(c)
        return None

    def buscarCelular(self, numero):
        lista = self.__leer_lista()
        for c in lista:
            if c["telefono"] == numero:
                return Cliente.from_dict(c)
        return None

    def __leer_lista(self):
        if os.path.exists(self.__nomA):
            with open(self.__nomA, 'r') as f:
                return json.load(f)
        return []

    def __escribir_lista(self, lista):
        with open(self.__nomA, 'w') as f:
            json.dump(lista, f, indent=4)