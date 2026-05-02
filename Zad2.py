x = float(input("wprowadź pierwszą liczbę"))
y = float(input("wprowadź drugą liczbę"))
z = float(input("wprowadź trzecią liczbę"))

if x > y and x > z and y > z:
    print(z, y, x)
elif y > x and y > z and x > z:
    print(z, x, y)
elif z > x and z > y and y > x:
    print(x, y, z)
elif x > z and x > y and z > y:
    print(y, z, x)
elif y > x and y > z and z > x:
    print(x, z, y)
elif z > x and z > y and x > y:
    print(y, x, z)