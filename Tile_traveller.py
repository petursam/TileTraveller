print("You can travel (N)orth.")
def one_one(d):
    if d == "N":
        return "You can travel: (N)orth, (E)ast or (S)outh"
    elif d == "n":
        return "You can travel: (N)orth, (E)ast or (S)outh"
        
    else: return "Not a valid direction!"
    


direction = input("Direction: ")

print(one_one(direction))
input("Direction: ")