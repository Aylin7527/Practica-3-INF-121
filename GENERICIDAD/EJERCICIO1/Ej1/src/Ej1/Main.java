package Ej1;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Primera Instancia de Caja ---");
        Caja<String> cajaTexto = new Caja<>();
        cajaTexto.guardar("Hola, ¿cómo estás?");
        System.out.println(cajaTexto.obtener(0));

        System.out.println("--- Segunda Instancia de Caja ---");
        Caja<Integer> cajaNumero = new Caja<>();
        cajaNumero.guardar(12345);
        System.out.println(cajaNumero.obtener(0));
    }
}