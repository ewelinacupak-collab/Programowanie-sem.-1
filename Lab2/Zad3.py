Nazwa_pliku = "Raport_maj.xlsx"

print(Nazwa_pliku)

x = Nazwa_pliku.endswith(".xlsx")
print(x)

if x == True:
    print("tak")
else:
    print("nie")
