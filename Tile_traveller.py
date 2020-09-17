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


def one_one():
    print(north)
    d = input("Direction: ")
    if d == "N" or d == "n":
        one_two()
    else: 
        print("Not a valid direction!")
        one_one()

def one_two():
    print(north_east_south)
    d = input("Direction: ")
    if d == "S" or d == "s":
        one_one()
    elif d == "E" or d == "e":
        two_two()
    elif d == "N" or d == "n":
        one_three()
    else:
        print("Not a valid direction!")
        one_two()

def one_three():
    print(east_south)
    d = input("Direction: ")
    if d == "E" or d == "e":
        two_three()
    elif d == "S" or d == "s":
        one_two()
    else:
        print("Not a valid direction!")
        one_three()

def two_three():
    print(east_west)
    d = input("Direction: ")
    if d == "E" or d == "e":
        three_three()
    elif d == "W" or d == "w":
        one_three()
    else:
        print("Not a valid direction!")
        two_three()

def two_two():
    print(south_west)
    d = input("Direction: ")
    if d == "S" or d == "s":
        two_one()
    elif d == "W" or d == "w":
        one_two()
    else:
        print("Not a valid direction!")
        two_two()

def two_one():
    print(north)
    d = input("Direction: ")
    if d == "N" or d == "n":
        two_two()
    else:
        print("Not a valid direction!")
        two_one()

def three_three():
    print(south_west)
    d = input("Direction: ")
    if d == "S" or d == "s":
        three_two()
    elif d == "W" or d == "w":
        two_three()
    else:
        print("Not a valid direction")
        three_three()

def three_two():
    print(north_south)
    d = input("Direction: ")
    if d == "N" or d == "n":
        three_three()
    elif d == "S" or d == "s":
        three_one()
    else:
        print("Not a valid direction")
        three_two()

def three_one():
    print("Victory!")

    
    

one_one()

