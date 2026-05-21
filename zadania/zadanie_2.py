"""
Zadanie 1: Zaawansowana obsługa wyjątków.
Program ma pobierać od użytkownika liczbę i dzielić przez nią liczbę 100.
Zabezpiecz program przed dwoma błędami:
1. Wpisaniem tekstu zamiast liczby (ValueError).
2. Próbą dzielenia przez zero (ZeroDivisionError).
"""

try:
    liczba = int(input("Podaj liczbę, przez którą mam podzielić 100: "))
    wynik = 100 / liczba
    print(f"Wynik to: {wynik}")

# -------------------------------------------------------------
# Do zrobienia: Obsłuż odpowiednie wyjątki poniżej, 
# aby program nie crashował, tylko wypisywał ładne komunikaty.
# -------------------------------------------------------------

except Exception as e:
    print(f"Wystąpił nieznany błąd: {e}")
