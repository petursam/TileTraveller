print("You can travel (N)orth.")

north = "You can travel (N)orth"
east = "You can travel (E)ast"
west = "You can travel (W)est"
south = "You can travel (S)outh"
north_west = "You can travel (N)orth or (W)est"
north_south = "You can travel (N)orth or (S)outh"
north_east = "You can travel (N)orth or (S)south"
north_east_south = "You can travel (N)orth or (E)ast or (S)outh"
east_south = "You can travel (E)ast or (S)outh"
east_west = "You can travel (E)ast or (W)est"
south_west = "You can travel (S)outh or (W)est"

def one_one(d):
    if d == "N" or d == "n":
        return north_east_south
        
    else: return "Not a valid direction!"

def one_two(d):
    if d == "S":
        return one_one(direction)
    else: return "hello world"
    
direction = input("Direction: ")

print(one_one(direction))
direction = input("Direction: ")