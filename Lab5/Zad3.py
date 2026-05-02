def parzyste(*args):
    return list(filter(lambda x: x % 2 == 0, args))
print(parzyste(1, 2, 3))
print(parzyste(1, 2, 3, 4))
