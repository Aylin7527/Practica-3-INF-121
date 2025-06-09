package Ej3;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ArchivoCliente {
    private String nombreArchivo;

    public ArchivoCliente(String nombreArchivo) {
        this.nombreArchivo = nombreArchivo;
    }

    public void crearArchivo() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo))) {
            oos.writeObject(new ArrayList<Cliente>());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void guardaCliente(Cliente cliente) {
        List<Cliente> lista = leerLista();
        lista.add(cliente);
        escribirLista(lista);
        System.out.println("Grabado: " + cliente);
    }

    public Cliente buscarCliente(int id) {
        List<Cliente> lista = leerLista();
        for (Cliente c : lista) {
            if (c.getId() == id) {
                return c;
            }
        }
        return null;
    }

    public Cliente buscarCelularCliente(int telefono) {
        List<Cliente> lista = leerLista();
        for (Cliente c : lista) {
            if (c.getTelefono() == telefono) {
                return c;
            }
        }
        return null;
    }

    @SuppressWarnings("unchecked")
    private List<Cliente> leerLista() {
        File archivo = new File(nombreArchivo);
        if (!archivo.exists()) {
            return new ArrayList<>();
        }
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            return (List<Cliente>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }

    private void escribirLista(List<Cliente> lista) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo))) {
            oos.writeObject(lista);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}