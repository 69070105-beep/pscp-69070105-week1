c1 = input()
c2 = input()

mix = {c1, c2}

if mix == {"Yellow", "Blue"}:
    print("Green")
elif mix == {"Blue", "Red"}:
    print("Violet")
elif mix == {"Red", "Yellow"}:
    print("Orange")
else:
    print("Error")