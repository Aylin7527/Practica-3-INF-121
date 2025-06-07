package Ej1;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ArchivoEmpleado {
    private String nombreArchivo;

    public ArchivoEmpleado(String nombreArchivo) {
        this.nombreArchivo = nombreArchivo;
    }

    public void guardarEmpleado(Empleado e) {
        List<Empleado> lista = leerLista();
        lista.add(e);
        escribirLista(lista);
    }

    @SuppressWarnings("unchecked")
    public List<Empleado> leerLista() {
        List<Empleado> lista = new ArrayList<>();
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            lista = (List<Empleado>) ois.readObject();
        } catch (FileNotFoundException | EOFException ex) {
        } catch (IOException | ClassNotFoundException ex) {
            ex.printStackTrace();
        }
        return lista;
    }

    public void escribirLista(List<Empleado> lista) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo))) {
            oos.writeObject(lista);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public Empleado buscaEmpleado(String nombre) {
        List<Empleado> lista = leerLista();
        for (Empleado e : lista) {
            if (e.getNombre().equalsIgnoreCase(nombre)) {
                return e;
            }
        }
        return null;
    }

    public Empleado mayorSalario(float salario) {
        List<Empleado> lista = leerLista();
        for (Empleado e : lista) {
            if (e.getSalario() > salario) {
                return e;
            }
        }
        return null;
    }
}