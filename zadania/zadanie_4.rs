/*
ZADANIE: Bezpieczne dzielenie w Rust.
Stworzyliśmy funkcję "bezpieczne_dzielenie", która zwraca Ok(wynik) 
lub Err("Nie można dzielić przez zero!").

Twoje zadanie: 
Wzorując się na przykładzie wyżej, użyj konstrukcji "match", aby sprawdzić 
zawartość zmiennej "wynik_dzielenia" i wypisać odpowiedni komunikat.
*/

fn bezpieczne_dzielenie(a: i32, b: i32) -> Result<i32, &'static str> {
    if b == 0 {
        Err("Nie można dzielić przez zero!")
    } else {
        Ok(a / b)
    }
}

fn main() {
    println!("--- Start programu ---");

    let wynik_dzielenia = bezpieczne_dzielenie(10, 0);

    // TODO: Tutaj wpisz konstrukcję match wynik_dzielenia { ... }
    // Jeśli Ok(w) -> wypisz "Wynik to: X"
    // Jeśli Err(e) -> wypisz błąd na ekran
    


    println!("--- Koniec programu ---");
}
