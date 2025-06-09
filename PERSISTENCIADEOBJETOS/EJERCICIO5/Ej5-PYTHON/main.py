from Medicamento import Medicamento
from Farmacia import Farmacia
from ArchFarmacia import ArchFarmacia

arch = ArchFarmacia("PERSISTENCIADEOBJETOS\EJERCICIO5\Ej5-PYTHON\Ej5-farmacias.json")
arch.crearArchivo()

f1 = Farmacia("Cruz Verde", 1, "Av. Siempre Viva 123")
f1.adicionarMedicamento(Medicamento("Golpex", 101, "Dolor", 25.5))
f1.adicionarMedicamento(Medicamento("Resfrix", 102, "Resfrio", 15.0))

f2 = Farmacia("PharmaPlus", 2, "Calle Falsa 456")
f2.adicionarMedicamento(Medicamento("Tosivital", 201, "Tos", 30.0))
f2.adicionarMedicamento(Medicamento("Frixol", 202, "Resfrio", 18.0))

f3 = Farmacia("Farmacia Vida", 3, "Plaza Central 789")
f3.adicionarMedicamento(Medicamento("Gripalex", 301, "Resfrio", 20.0))

arch.adicionar(f1)
arch.adicionar(f2)
arch.adicionar(f3)

print("\n=== MOSTRAR TODAS LAS FARMACIAS ===")
arch.listar()

print("\n Medicamentos para la TOS - Sucursal 2")
lista = arch._ArchFarmacia__leerArchivo()
for fdict in lista:
    if fdict["sucursal"] == 2:
        f = arch._ArchFarmacia__dictToFarmacia(fdict)
        f.mostrarMedicamentos("Tos")

med_buscar = "Golpex"
print(f"\nFarmacia que tiene '{med_buscar}':")
lista = arch._ArchFarmacia__leerArchivo()
encontrado = False
for fdict in lista:
    f = arch._ArchFarmacia__dictToFarmacia(fdict)
    if f.buscaMedicamento(med_buscar):
        print(f"Sucursal: {f.getSucursal()}, Dirección: {f.getDireccion()}")
        encontrado = True
        break
if not encontrado:
    print("No se encontró ninguna farmacia con ese medicamento.")
