"""สลับหมายเลข"""

NUM = int(input())
WAY = input()

MUN = int(str(NUM)[::-1])

if WAY == "+":
    print(f"{NUM} + {MUN} = {NUM + MUN}")
else:
    print(f"{NUM} * {MUN} = {NUM * MUN}")
