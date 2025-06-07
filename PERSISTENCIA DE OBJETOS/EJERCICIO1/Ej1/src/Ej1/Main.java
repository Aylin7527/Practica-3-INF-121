package Ej1;

public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");

        Empleado[] empleados = {
            new Empleado("Carlos", 30, 4000),
            new Empleado("Ana", 28, 6000),
            new Empleado("Luis", 45, 3500),
            new Empleado("Marta", 40, 7000),
            new Empleado("José", 32, 3000)
        };

        for (Empleado e : empleados) {
            archivo.guardarEmpleado(e);
        }

        System.out.println("\nBuscar empleado 'Carlos':");
        Empleado encontrado = archivo.buscaEmpleado("Carlos");
        System.out.println(encontrado != null ? encontrado : "Empleado no encontrado.");

        System.out.println("\nBuscar empleado con salario mayor a 4500:");
        Empleado mayor = archivo.mayorSalario(4500);
        System.out.println(mayor != null ? mayor : "No hay empleado con salario mayor al ingresado.");
    }
}