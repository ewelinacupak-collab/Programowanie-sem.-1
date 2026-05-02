# Zadanie 6

droga = float(input("Podaj drogę w km:"))
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = 6.5
print ("cena paliwa za litr = 6.5 zł")

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print ("Samochód spali", zuzycie_paliwa, "litrów paliwa", end=("\n"))

print ("Koszt wyniesie", koszt, "zł")
