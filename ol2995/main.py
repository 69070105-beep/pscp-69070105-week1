"""การตรวจสอบบัตรนักศึกษา"""

NAME = int(input())
NAME1 = str(NAME)

if NAME1[2] == "1" and NAME1[3] == "6":
    print("yes")
else:
    print("no")
