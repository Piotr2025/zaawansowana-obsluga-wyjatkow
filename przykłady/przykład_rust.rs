// PRZYKŁAD: Bezpieczna zamiana tekstu na liczbę

fn main() {
    let tekst = "123";

    // Funkcja .parse() nie rzuca błędu, tylko zwraca typ Result
    let wynik: Result<i32, _> = tekst.parse();

    // Używamy "match", żeby sprawdzić, co jest w środku paczki
    match wynik {
        Ok(liczba) => {
            // Jeśli wszystko poszło dobrze (Ok), mamy dostęp do liczby
            println!("Sukces! Liczba to: {}", liczba);
        }
        Err(_) => {
            // Jeśli coś poszło nie tak (Err), program nie crashuje, tylko robi to:
            println!("Przykład: To nie jest poprawna liczba!");
        }
    }
}
