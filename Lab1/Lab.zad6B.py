# Zadanie 6b1

droga = float(input("Podaj drogę w km:"))
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = 6.5
print ("cena paliwa za litr = 6.5 zł")

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print (f"Samochód spali {zuzycie_paliwa} litrów paliwa")
print (f"Koszt wyniesie {koszt} zł")

# Zadanie 6b2

print (end="\n")

import random

los = random.randint(1, 20000)
droga = los
print ("Droga wynosi", droga)
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = float(input("Podaj cenę paliwa za litr:"))

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print (f"Samochód spali {zuzycie_paliwa} litrów paliwa")
print (f"Koszt wyniesie {koszt} zł")
