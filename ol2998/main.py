"""EuclideanDistance2D"""
import math as m

q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())

total = (q1 - p1) ** 2
total1 = (q2 - p2) ** 2
total2 = m.sqrt(total + total1)

print(total2)
