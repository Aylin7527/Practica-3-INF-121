from Medicamento import Medicamento

class Farmacia:
    def __init__(self, nombreFarmacia="", sucursal=0, direccion=""):
        self.__nombreFarmacia = nombreFarmacia
        self.__sucursal = sucursal
        self.__direccion = direccion
        self.__nroMedicamentos = 0
        self.__m = []

    def leer(self):
        self.__nombreFarmacia = input("Nombre de la farmacia: ")
        self.__sucursal = int(input("Número de sucursal: "))
        self.__direccion = input("Dirección: ")
        n = int(input("Cantidad de medicamentos: "))
        for _ in range(n):
            med = Medicamento()
            med.leer()
            self.adicionarMedicamento(med)

    def mostrar(self):
        print(f"Farmacia: {self.__nombreFarmacia}, Sucursal: {self.__sucursal}, Dirección: {self.__direccion}")
        if self.__nroMedicamentos == 0:
            print("  Sin medicamentos.")
        for med in self.__m:
            med.mostrar()

    def getDireccion(self):
        return self.__direccion

    def getSucursal(self):
        return self.__sucursal

    def mostrarMedicamentos(self, tipo):
        for med in self.__m:
            if med.getTipo().lower() == tipo.lower():
                med.mostrar()

    def buscaMedicamento(self, nombreMed):
        for med in self.__m:
            if med.getNombre().lower() == nombreMed.lower():
                return True
        return False

    def adicionarMedicamento(self, medicamento):
        if self.__nroMedicamentos < 100:
            self.__m.append(medicamento)
            self.__nroMedicamentos += 1
        else:
            print("¡Límite de 100 medicamentos alcanzado!")

    def getListaMedicamentos(self):
        return self.__m