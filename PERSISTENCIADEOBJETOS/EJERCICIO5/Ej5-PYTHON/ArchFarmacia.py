import json
from Farmacia import Farmacia
from Medicamento import Medicamento

class ArchFarmacia:
    def __init__(self, nombre_archivo):
        self.__na = nombre_archivo

    def crearArchivo(self):
        with open(self.__na, "w") as f:
            json.dump([], f)

    def adicionar(self, farmacia):
        lista = self.__leerArchivo()
        lista.append(self.__farmaciaToDict(farmacia))
        self.__guardarArchivo(lista)

    def listar(self):
        lista = self.__leerArchivo()
        for fdict in lista:
            f = self.__dictToFarmacia(fdict)
            f.mostrar()

    def mostrarMedicamentosResfrios(self):
        lista = self.__leerArchivo()
        print("Medicamentos para el resfrío:")
        for fdict in lista:
            f = self.__dictToFarmacia(fdict)
            f.mostrarMedicamentos("Resfrio")

    def precioMedicamentoTos(self):
        lista = self.__leerArchivo()
        for fdict in lista:
            f = self.__dictToFarmacia(fdict)
            for med in f.getListaMedicamentos():
                if med.getTipo().lower() == "tos":
                    return med.getPrecio() 
        return 0.0 

    def mostrarMedicamentosMenorTos(self):
        precio_limite = self.precioMedicamentoTos()
        if precio_limite == 0.0:
            print("No hay medicamentos para la Tos registrados.")
            return

        print(f"\nMedicamentos para la Tos con precio menor a {precio_limite}:")
        lista = self.__leerArchivo()
        for fdict in lista:
            f = self.__dictToFarmacia(fdict)
            for med in f.getListaMedicamentos():
                if med.getTipo().lower() == "tos" and med.getPrecio() < precio_limite:
                    print(f"- {med.getNombre()} ({med.getPrecio()}) - Sucursal: {f.getSucursal()}")

    def __leerArchivo(self):
        try:
            with open(self.__na, "r") as f:
                return json.load(f)
        except:
            return []

    def __guardarArchivo(self, lista):
        with open(self.__na, "w") as f:
            json.dump(lista, f, indent=4)

    def __farmaciaToDict(self, farmacia):
        return {
            "nombreFarmacia": farmacia._Farmacia__nombreFarmacia,
            "sucursal": farmacia._Farmacia__sucursal,
            "direccion": farmacia._Farmacia__direccion,
            "medicamentos": [
                {
                    "nombre": m._Medicamento__nombre,
                    "codMedicamento": m._Medicamento__codMedicamento,
                    "tipo": m._Medicamento__tipo,
                    "precio": m._Medicamento__precio
                } for m in farmacia.getListaMedicamentos()
            ]
        }

    def __dictToFarmacia(self, data):
        f = Farmacia(data["nombreFarmacia"], data["sucursal"], data["direccion"])
        for m in data["medicamentos"]:
            med = Medicamento(
                m["nombre"],
                m["codMedicamento"],
                m["tipo"],
                m["precio"]
            )
            f.adicionarMedicamento(med)
        return f
