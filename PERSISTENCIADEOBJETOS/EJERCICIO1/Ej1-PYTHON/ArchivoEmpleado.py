import json
import os
from Empleado import Empleado

class ArchivoEmpleado:
    def __init__(self, nombre_archivo):
        self.__nombre_archivo = nombre_archivo

    def crearArchivo(self):
        """Crea un archivo JSON vacío."""
        with open(self.__nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)

    def guardarEmpleado(self, e):
        lista = self.__leer_lista()
        lista.append({
            'nombre': e.get_nombre(),
            'edad': e.get_edad(),
            'salario': e.get_salario()
        })
        self.__escribir_lista(lista)

    def buscaEmpleado(self, nombre):
        lista = self.__leer_lista()
        for emp in lista:
            if emp['nombre'].lower() == nombre.lower():
                return emp
        return None

    def mayorSalario(self, salario):
        lista = self.__leer_lista()
        for emp in lista:
            if emp['salario'] > salario:
                return emp
        return None

    def __leer_lista(self):
        if os.path.exists(self.__nombre_archivo):
            with open(self.__nombre_archivo, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def __escribir_lista(self, lista):
        with open(self.__nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4)
