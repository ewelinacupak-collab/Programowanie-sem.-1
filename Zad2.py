Lista = ["Jan", "Jakub", "Oliwia", "Emilia"]
print(Lista)

print("Posortowana", sorted(Lista))

Lista.append("Julia")
Lista.append("Iwona")
print(Lista)

print("Ostatni element:", Lista.pop())

Lista.insert(3, "Maciej")
print(Lista)

Lista.reverse()
print(Lista)

print(Lista*2)
