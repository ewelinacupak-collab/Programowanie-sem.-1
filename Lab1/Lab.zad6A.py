# Zadanie 6a

import random

los = random.randint(1, 20000)
droga = los
print ("Droga wynosi", droga)
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = float(input("Podaj cenę paliwa za litr:"))

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print ("Samochód spali", zuzycie_paliwa, "litrów paliwa", end=("\n"))

print ("Koszt wyniesie", koszt, "zł")
