with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\n")
    plik.write("ALR, 113")

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)