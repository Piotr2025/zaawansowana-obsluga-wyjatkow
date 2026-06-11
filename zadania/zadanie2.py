try:
    liczba = int(input("Podaj liczbę, przez którą chesz podzielić liczbę 100: "))
    wynik = 100 / liczba
    print(f"Wynik to: {wynik}")

# TODO: Obsłuż ValueError oraz ZeroDivisionError, wypisując dedykowane komunikaty 
#       dla każdego z tych błędów.

except Exception as e:
    print(f"Wystąpił nieznany błąd: {e}")
