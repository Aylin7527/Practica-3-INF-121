package Ej5;

public class Main {
	public static void main(String[] args) {
        System.out.println("--- Prueba con enteros ---");
        Pila<Integer> pilaInt = new Pila<>();
        pilaInt.apilar(1);
        pilaInt.apilar(2);
        pilaInt.apilar(3);
        pilaInt.mostrar();
        System.out.println("Desapilado: " + pilaInt.desapilar());
        System.out.println("**** Después del Desapilado ****");
        pilaInt.mostrar();

        System.out.println("--- Prueba con cadenas ---");
        Pila<String> pilaStr = new Pila<>();
        pilaStr.apilar("a");
        pilaStr.apilar("b");
        pilaStr.apilar("c");
        pilaStr.mostrar();
        System.out.println("Desapilado: " + pilaStr.desapilar());
        System.out.println("**** Después del Desapilado ****");
        pilaStr.mostrar();

        System.out.println("--- Prueba con flotantes ---");
        Pila<Double> pilaFloat = new Pila<>();
        pilaFloat.apilar(1.1);
        pilaFloat.apilar(2.2);
        pilaFloat.apilar(3.3);
        pilaFloat.mostrar();
        System.out.println("Desapilado: " + pilaFloat.desapilar());
        System.out.println("**** Después del Desapilado ****");
        pilaFloat.mostrar();
    }

}