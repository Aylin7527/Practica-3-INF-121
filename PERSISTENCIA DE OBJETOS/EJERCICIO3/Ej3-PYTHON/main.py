from ArchivoCliente import ArchivoCliente
from Cliente import Cliente

nombre_archivo = "clientes.dat"
archivo = ArchivoCliente(nombre_archivo)

# Crear archivo vacío
archivo.crearArchivo()

clientes = [
    Cliente(1, "Juan Pérez", 78945612),
    Cliente(2, "Lucía Gómez", 76543210),
    Cliente(3, "Carlos Rojas", 71234567),
    Cliente(4, "Ana Torres", 70112233),
    Cliente(5, "Marco Díaz", 79887766)
]

for cliente in clientes:
    archivo.guardaCliente(cliente)
    print(f"Grabado: {cliente}")

print("\n--- Buscar cliente por ID (2) ---")
resultado = archivo.buscarCliente(2)
print(resultado if resultado else "No encontrado")

print("\n--- Buscar cliente por celular (71234567) ---")
resultado = archivo.buscarCelular(71234567)
print(resultado if resultado else "No encontrado")