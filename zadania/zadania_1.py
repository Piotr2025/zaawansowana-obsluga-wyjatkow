"""
ZADANIE 1: Zabezpiecz program przed błędnym wpisaniem danych.
Jeśli użytkownik zamiast liczby wpisze litery (np. "trzy"), 
funkcja int() rzuci błąd ValueError.

Twoje zadanie: Użyj try i except ValueError, aby program się nie wykrzywił.
"""

print("--- Start programu ---")

# TODO: Tutaj otwórz blok try:
tekst = "trzy"
liczba = int(tekst)  # <-- To rzuci błąd ValueError!
print(f"Udało się! Liczba to: {liczba}")

# TODO: Tutaj użyj except ValueError: i wypisz komunikat "To nie jest liczba!"


print("--- Koniec programu (Udało się doprowadzić program do końca!) ---")
