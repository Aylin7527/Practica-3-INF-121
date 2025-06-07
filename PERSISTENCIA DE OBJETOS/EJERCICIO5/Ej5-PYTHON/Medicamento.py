class Medicamento:
    def __init__(self, nombre="", codMedicamento=0, tipo="", precio=0.0):
        self.__nombre = nombre
        self.__codMedicamento = codMedicamento
        self.__tipo = tipo
        self.__precio = precio

    def leer(self):
        self.__nombre = input("Nombre del medicamento: ")
        self.__codMedicamento = int(input("Código: "))
        self.__tipo = input("Tipo (Tos / Resfrio / Otro): ")
        self.__precio = float(input("Precio: "))

    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Código: {self.__codMedicamento}, Tipo: {self.__tipo}, Precio: Bs{self.__precio:.2f}")

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio

    def getNombre(self):
        return self.__nombre