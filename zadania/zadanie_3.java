/*
ZADANIE 1: Zabezpiecz program przed dzieleniem przez zero.
W Javie próba podzielenia liczby całkowitej przez 0 wyrzuca błąd ArithmeticException.

Twoje zadanie: 
Uzupełnij brakujące sekcje try oraz catch (ArithmeticException...), 
aby program zamiast się wywalić, wypisał: "Błąd: Nie dziel przez zero!".
*/

public class Zadanie {
    public static void main(String[] args) {
        System.out.println("--- Start programu ---");

        // TODO: Tutaj otwórz blok try {
        
        int wynik = 50 / 0; // <-- To rzuci ArithmeticException
        System.out.println("Wynik to: " + wynik);
        
        // TODO: Tutaj zamknij try i dodaj catch (ArithmeticException zmienna) {
        // i wypisz komunikat systemowy
        
        // }

        System.out.println("--- Koniec programu (Udało się!) ---");
    }
}
