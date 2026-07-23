"""Safe Password"""

w = input()
num = int(input())

if w == "H" and num == 4567:
    print("safe unlocked")
elif w == "H" and num != 4567:
    print("safe locked - change digit")
elif w != "H" and num == 4567:
    print("safe locked - change char")
else:
    print("safe locked")
