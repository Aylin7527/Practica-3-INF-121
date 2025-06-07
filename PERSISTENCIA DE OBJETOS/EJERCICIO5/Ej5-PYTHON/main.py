from Medicamento import Medicamento
from Farmacia import Farmacia
from ArchFarmacia import ArchFarmacia

arch = ArchFarmacia("farmacias.dat")
arch.crearArchivo()

f1 = Farmacia("Cruz Verde", 1, "Av. Siempre Viva 123")
f1.adicionarMedicamento(Medicamento("Golpex", 101, "Tos", 25.5))
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

sucursal_consulta = 2
arch.mostrarMedicamentosTos(sucursal_consulta)

arch.buscarFarmaciaPorMedicamento("Golpex")