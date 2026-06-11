nazwa_pliku = input("Podaj nazwę pliku do otwarcia (np. dane.txt): ")

try:
    # Próbujemy otworzyć i przeczytać plik
    with open(nazwa_pliku, "r") as plik:
        print(plik.read())

# 1. TUTAJ: Dopisz odpowiedni typ błędu (wyjątku)
except ???:
    # 2. TUTAJ: Dopisz linijkę, która wyświetli ładny komunikat dla użytkownika
    ???
