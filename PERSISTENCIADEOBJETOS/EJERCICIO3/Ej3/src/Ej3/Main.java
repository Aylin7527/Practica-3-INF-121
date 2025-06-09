package Ej3;
public class Main {
    public static void main(String[] args) {
        String nombreArchivo = "Ej3-clientes.dat";

        ArchivoCliente archivoCliente = new ArchivoCliente(nombreArchivo);
        archivoCliente.crearArchivo();

        Cliente[] clientes = {
            new Cliente(1, "Juan Pérez", 78945612),
            new Cliente(2, "Lucía Gómez", 76543210),
            new Cliente(3, "Carlos Rojas", 71234567),
            new Cliente(4, "Ana Torres", 70112233),
            new Cliente(5, "Marco Díaz", 79887766)
        };

        for (Cliente c : clientes) {
            archivoCliente.guardaCliente(c);
        }

        System.out.println("\n--- Buscar cliente por ID (2) ---");
        Cliente c1 = archivoCliente.buscarCliente(2);
        System.out.println(c1 != null ? c1 : "No encontrado");

        System.out.println("\n--- Buscar cliente por celular (71234567) ---");
        Cliente c2 = archivoCliente.buscarCelularCliente(71234567);
        System.out.println(c2 != null ? c2 : "No encontrado");
    }
}