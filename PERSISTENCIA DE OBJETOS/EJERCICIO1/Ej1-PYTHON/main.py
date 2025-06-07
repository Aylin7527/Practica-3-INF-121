from ArchivoEmpleado import ArchivoEmpleado
from Empleado import Empleado

archivo = ArchivoEmpleado("empleados.dat")

empleados = [
    Empleado("Carlos", 30, 4000),
    Empleado("Ana", 28, 6000),
    Empleado("Luis", 45, 3500),
    Empleado("Marta", 40, 7000),
    Empleado("José", 32, 3000)
]

for e in empleados:
    archivo.guardarEmpleado(e)

print("\nBuscar empleado 'Carlos':")
emp = archivo.buscaEmpleado("Carlos")
print(emp if emp else "Empleado no encontrado.")

print("\nBuscar empleado con salario mayor a 4500:")
emp = archivo.mayorSalario(4500)
print(emp if emp else "No hay empleado con salario mayor al ingresado.")