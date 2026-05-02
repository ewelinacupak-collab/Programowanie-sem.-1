import numpy as np

u = np.random.default_rng(42)

mac = u.normal(0,1,(6,4))
print(mac)

print("--------")

print(np.mean(mac, axis=0))

print("------")

min_ind = np.argmin(mac, axis=0)
print(min_ind)

print("--------")

max_ind = np.argmax(mac, axis=0)
print(max_ind)

print("--------")



