"""การตรวจสอบสระ"""
L = ["a","e","i","o","u"]
word = input().lower()
Y = len(word)
if Y == 1:
    if word in L:
        print("yes")
    else: print("no")
