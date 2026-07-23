"""หาระยะทางระหว่างจุด 3D"""
import math as m
x3, y3, z3= input().split()
x4, y4, z4= input().split()

x1 = int(x3)
y1 = int(y3)
z1 = int(z3)
x2 = int(x4)
y2 = int(y4)
z2 = int(z4)

tx = (x1 - x2) ** 2
ty = (y1 - y2) ** 2
tz = (z1 - z2) ** 2
total = m.sqrt(tx + ty + tz)

print(f"{total:.2f}")
