"""Heron of Alexandria"""

import math as m

a = float(input())
b = float(input())
c = float(input())

abc = a + b + c
abc1 = abc / 2
abc3 = (abc1 - a ) * (abc1 - b) * (abc1 - c)
abc4 = m.sqrt(abc1 * abc3)

print(f"{abc4:.3f}")
