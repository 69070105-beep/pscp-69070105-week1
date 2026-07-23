"""กระต่ายน้อยล้อมรั้วลวดหนาม"""

x, y, z= input().split()
h = int(input())

x1 = int(x)
y1 = int(y)
z1 = int(z)

sq = (x1 + y1) * 2
sq1 = sq * z1
sq2 = sq1 * h

print(sq1)
print(sq2)
