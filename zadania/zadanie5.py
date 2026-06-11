nazwa_pliku = input("Podaj nazwę pliku do otwarcia (np. dane.txt): ")

try:
    with open(nazwa_pliku, "r") as plik:
        print(plik.read())

# 1. TODO: Dopisz odpowiedni typ błędu dla braku pliku (FileNotFoundError)
except ???:

# 2. TODO: Dopisz linijkę, która wyświetli komunikat dla użytkownika
    ???
