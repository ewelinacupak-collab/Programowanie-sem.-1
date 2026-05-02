Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(Moja_lista)

print("Pierwszy element:", Moja_lista[0])

print("Ostatni element", Moja_lista[-1])

print("Długość listy:", len(Moja_lista))

print("Element największy:", max(Moja_lista))

print("Element najmniejszy:", min(Moja_lista))

print("Suma elementów:", sum(Moja_lista))

print("Elementy posortowane:", sorted(Moja_lista))

Moja_lista.append(6)
print("Dodanie elementu 6 do listy:", Moja_lista)

Moja_lista.insert(2,7)
print("Dodanie elementu 7 do listy:", Moja_lista)

usuniety_element = Moja_lista.pop()
print("Usuniety element", usuniety_element)
print("Lista bez usunietego elementu", Moja_lista)

Moja_lista.reverse()
print("Odwrócenie kolejności", Moja_lista)

kolejna = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Lista nr 2:", kolejna)

print("Listy połączone:", Moja_lista + kolejna)

print("Pięciokrotne powtórzenie wartości pierwszej listy:", Moja_lista*5)

print("Wycinek listy od poczatklu do elementu wybranego:", Moja_lista[:6])

print("Od elementu do końca:", Moja_lista[3:])

print("Zakres elementów z krokiem n", Moja_lista[3:15:2])

print("Odwrócenie listy", Moja_lista[::-1])


