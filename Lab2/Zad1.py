x = int(input("Podaj liczbę zdobytych punktów"))
if x > 80:
    print("Egzamin zdany w terminie 0")
elif x > 50:
    print("Wynik może zostać poprawiony")
else:
    print("Egzamin do poprawy")