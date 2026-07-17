"""Cyan's password generator"""

NAME = input()
SURNAME = input()
AGE = input()

if len(NAME) >= 5 and len(SURNAME) >= 5:
    print(f"{NAME[:2]}{SURNAME[-1]}{AGE[-1]}")
else:
    print(f"{NAME[0]}{AGE}{SURNAME[-1]}")
