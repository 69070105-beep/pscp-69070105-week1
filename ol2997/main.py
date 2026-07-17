"""Elo"""

RA = int(input())
RB = int(input())
samakan = input()

if samakan == "A":
    total = RB - RA
else:
    total = RA - RB

total1 = total / 400
total2 = 10 ** total1
total3 = total2 + 1
total4 = 1 / total3

print(f"{total4:.2f}")
