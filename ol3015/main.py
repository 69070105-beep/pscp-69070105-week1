"""pro"""

PROSON = int(input())
PRO = int(input())
PAY = int(input())
TTPAY = int(input())

GROUP = TTPAY // PROSON
PPTTPAY = TTPAY % PROSON

print(((GROUP * PRO ) + PPTTPAY) * PAY)
