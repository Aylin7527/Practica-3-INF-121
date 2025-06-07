import pickle

class ArchFarmacia:
    def __init__(self, na):
        self.__na = na

    def crearArchivo(self):
        with open(self.__na, "wb") as f:
            pickle.dump([], f)

    def adicionar(self, farmacia):
        lista = self.__leerArchivo()
        lista.append(farmacia)
        self.__guardarArchivo(lista)

    def listar(self):
        lista = self.__leerArchivo()
        for f in lista:
            f.mostrar()

    def mostrarMedicamentosResfrios(self):
        lista = self.__leerArchivo()
        print("Medicamentos para el resfrío:")
        for f in lista:
            f.mostrarMedicamentos("Resfrio")

    def mostrarMedicamentosTos(self, sucursalX):
        lista = self.__leerArchivo()
        for f in lista:
            if f.getSucursal() == sucursalX:
                print(f"\n Medicamentos para la TOS - Sucursal {sucursalX}")
                f.mostrarMedicamentos("Tos")

    def buscarFarmaciaPorMedicamento(self, nombreMed):
        lista = self.__leerArchivo()
        for f in lista:
            if f.buscaMedicamento(nombreMed):
                print(f"\nFarmacia que tiene '{nombreMed}':")
                print(f"Sucursal: {f.getSucursal()}, Dirección: {f.getDireccion()}")

    def __leerArchivo(self):
        try:
            with open(self.__na, "rb") as f:
                return pickle.load(f)
        except:
            return []

    def __guardarArchivo(self, lista):
        with open(self.__na, "wb") as f:
            pickle.dump(lista, f)