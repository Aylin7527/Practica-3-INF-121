class Empleado:
    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_salario(self):
        return self.__salario

    def __str__(self):
        return f"Empleado: {self.__nombre}, Edad: {self.__edad}, Salario: {self.__salario}"