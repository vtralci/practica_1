from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, X1, Y1, adjacent, box, shine, stench, safe')
#adjacency rules
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X + 1) & (Y1 == Y)))
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X - 1) & (Y1 == Y)))
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X) & (Y1 == Y + 1)))
adjacent(X, Y, X1, Y1) <= (box(X, Y) & box(X1, Y1) & ((X1 == X) & (Y1 ==  Y - 1)))

#safety rules
safe(X, Y) <= box(X, Y) & breeze(X, Y)
safe(X, Y) <= box(X, Y) & shine(X, Y)
safe(X, Y) <= box(X, Y) & stench(X, Y)

#

#creating a 5x5 grid
for i in range(0, 5):
    for j in range(0, 5):
        +box(i+1, j+1)
print(f"Casillas: {box(X, Y).data}")


print(bool(adjacent(1, 1, 1, 2)))  # True
print(bool(adjacent(X, Y, 1, 1)))  # False
print(f"Adyacencias: {adjacent(X, Y, X1, X2).data}")