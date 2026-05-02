import numpy as np
a = np.arange(0,25).reshape(5,5)
print(a)

print(a[0,:])
print(a[1:,-1])
print(a[-1,:-1][::-1])
print(a[1:-1,0][::-1])

