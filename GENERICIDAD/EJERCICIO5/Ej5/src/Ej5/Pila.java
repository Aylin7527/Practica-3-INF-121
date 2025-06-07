package Ej5;

import java.util.ArrayList;
import java.util.List;

public class Pila<T> {
    private List<T> elementos;

    public Pila() {
        this.elementos = new ArrayList<>();
    }

    public void apilar(T item) {
        elementos.add(item);
    }

    public T desapilar() {
        if (elementos.isEmpty()) {
            throw new RuntimeException("La pila está vacía");
        }
        return elementos.remove(elementos.size() - 1);
    }

    public void mostrar() {
        System.out.println("Pila: " + elementos);
    }

}