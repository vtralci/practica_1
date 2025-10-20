from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, X1, Y1, adjacent, box, shine, stench, safe, breeze, goldLocation, unsafe, certain, X2, Y2, X3, Y3, X4, Y4, safeBreeze, safeStench, noPossibleWumpus, noPossiblePit')

#adjacency rules
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X + 1) & (Y1 == Y)))
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X - 1) & (Y1 == Y)))
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X) & (Y1 == Y + 1)))
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X) & (Y1 ==  Y - 1)))

#safety rules
safe(X, Y) <= box(X, Y) & breeze(X, Y)
safe(X, Y) <= box(X, Y) & shine(X, Y)
safe(X, Y) <= box(X, Y) & stench(X, Y)
safeBreeze(X, Y) <= box(X, Y) & adjacent(X1, Y1, X, Y) & breeze(X1, Y1) & adjacent(X2, Y2, X, Y) & box(X1, Y1) & box(X2, Y2) & (X1 != X2) & (Y1 != Y2) & ~breeze(X2, Y2)
safeStench(X, Y) <= box(X, Y) & adjacent(X1, Y1, X, Y) & stench(X1, Y1) & adjacent(X2, Y2, X, Y) & box(X1, Y1) & box(X2, Y2) & (X1 != X2) & (Y1 != Y2) & ~stench(X2, Y2)
safe(X, Y) <= safeBreeze(X, Y) & safeStench(X, Y)
goldLocation(X, Y) <= box(X, Y) & shine(X, Y)

noPossibleWumpus(X, Y) <= box(X, Y) & adjacent(X1, Y1, X, Y) & ~stench(X1, Y1) #Confirma si no hay Wumpus en (X,Y)

noPossiblePit(X, Y) <= box(X, Y) & adjacent(X1, Y1, X, Y) & ~breeze(X1, Y1) #Confirma si no hay hoyo en (X,Y)

for i in range(0, 4):
    for j in range(0, 4):
        +box(i+1, j+1)

#knowledge base
+stench(1, 4)
+stench(1, 2)
+stench(2, 3)
+breeze(2, 3)
+breeze(3, 2)
+breeze(4, 3)
+breeze(3, 4)
+breeze(2, 1)
+breeze(4, 1)
+shine(2, 3)

def bool_breeze_at(x, y):
    return bool(breeze(x, y))

def bool_stench_at(x, y):
    return bool(stench(x, y))

def bool_no_possible_pit(x, y):
    return bool(noPossiblePit(x, y))

def bool_no_possible_wumpus(x, y):
    return bool(noPossibleWumpus(x, y))

def bool_possible_pit(x, y):
    return not bool(noPossiblePit(x, y))

def safe_at(x, y):
    return bool(safe(x, y))

def main():
    while True:
        
        try:
            user_input = str(input("Enter coordinates (x y) to check safety or 'E' to quit: "))
            if user_input == 'E':
                break
            x = int(user_input.split()[0])
            y = int(user_input.split()[1])
            if 1 <= x <= 4 and 1 <= y <= 4:
                print(f"Breeze at ({x}, {y}): {bool_breeze_at(x, y)}")
                print(f"Stench at ({x}, {y}): {bool_stench_at(x, y)}")
                print(f"Possible pit at ({x}, {y}): {bool_possible_pit(x, y)}")
                print(f"No possible pit at ({x}, {y}): {bool_no_possible_pit(x, y)}")
                print(f"No possible Wumpus at ({x}, {y})?: {bool_no_possible_wumpus(x, y)}")
                print(f" Is it certain that ({x}, {y}) is safe?: {safe_at(x, y)}")
            else:
                print("Coordinates must be between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

main()
    
