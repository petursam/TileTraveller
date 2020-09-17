def first(n):
    if n == "N" or "n":
        input("You can travel: (N)orth, (E)ast or (S)outh")
    else: print("Not a valid direction!")


direction = input("Direction: ")

print(first(direction))