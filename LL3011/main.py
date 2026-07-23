"""color"""

c1 = input().strip()
c2 = input().strip()

if c1 == "Yellow" and c2 == "Blue":
    print("Green")
elif c1 == "Blue" and c2 == "Red":
    print("Violet")
elif c1 == "Red" and c2 == "Yellow":
    print("Orange")
elif c1 == "Blue" and c2 == "Yellow":
    print("Green")
elif c1 == "Red" and c2 == "Blue":
    print("Violet")
elif c1 == "Yellow" and c2 == "Red":
    print("Orange")
else:
    print("Error")
