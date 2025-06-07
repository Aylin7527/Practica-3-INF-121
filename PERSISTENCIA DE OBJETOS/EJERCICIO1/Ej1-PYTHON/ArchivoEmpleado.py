import pickle
import os
from Empleado import Empleado

class ArchivoEmpleado:
    def __init__(self, nombre_archivo):
        self.__nombre_archivo = nombre_archivo

    def guardarEmpleado(self, e):
        lista = self.__leer_lista()
        lista.append(e)
        self.__escribir_lista(lista)

    def buscaEmpleado(self, nombre):
        lista = self.__leer_lista()
        for emp in lista:
            if emp.get_nombre().lower() == nombre.lower():
                return emp
        return None

    def mayorSalario(self, salario):
        lista = self.__leer_lista()
        for emp in lista:
            if emp.get_salario() > salario:
                return emp
        return None

    def __leer_lista(self):
        if os.path.exists(self.__nombre_archivo):
            with open(self.__nombre_archivo, 'rb') as f:
                return pickle.load(f)
        else:
            return []

    def __escribir_lista(self, lista):
        with open(self.__nombre_archivo, 'wb') as f:
            pickle.dump(lista, f)