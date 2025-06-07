package Ej1;

import java.util.ArrayList;

public class Caja<T> {
    private ArrayList<T> contenido;

    public Caja() {
        contenido = new ArrayList<>();
    }

    public void guardar(T valor) {
        contenido.add(valor);
    }

    public T obtener(int i) {
        if (i < 0 || i >= contenido.size()) {
            System.out.println("Índice fuera de rango.");
            return null;
        } else {
            return contenido.get(i);
        }
    }
}