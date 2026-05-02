import numpy as np

A = np.arange(1, 7).reshape(2, 3)
B = np.arange(7, 13).reshape(3, 2)

print(A)
print("---------")
print(B)

print("---------")

print(A@B)
print("---------")
print(B@A)

print("---------")

BB = np.arange(1,10).reshape(3,3)
print(BB)

print("---------")

print(A@BB)
print("---------")
print(BB@A)
print("---------")