from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, X1, Y1, adjacent, box, shine, stench, safe, breeze, possibleNearWumpus, possibleNearPit, goldLocation, unsafe, certain, pit, wumpus')
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
possibleNearWumpus(X1, Y1) <= box(X, Y) & adjacent(X, Y, X1, Y1) & stench(X, Y)
possibleNearPit(X1, Y1) <= box(X, Y) & adjacent(X, Y, X1, Y1) & breeze(X, Y)
goldLocation(X, Y) <= box(X, Y) & shine(X, Y)

unsafe(X, Y) <= box(X, Y) & wumpus(X, Y)
unsafe(X, Y) <= box(X, Y) & pit(X, Y)

certain(X, Y) <= box(X, Y) & safe(X, Y) 
certain(X, Y) <= box(X, Y) & unsafe(X, Y)




#creating a 5x5 grid
for i in range(0, 5):
    for j in range(0, 5):
        +box(i+1, j+1)


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
+wumpus(1, 3)
+pit(3, 3)
+pit(3, 1)
+pit(4, 4)

print(f"Breeze locations: {breeze(X,Y).data}")
print(f"Safe locations: {safe(X,Y).data}")
print(f"Unsafe locations: {unsafe(X,Y).data}")
print(f"Certain locations: {certain(X,Y).data}")
print(f"Certeza de 1,1 seguro? => {bool(certain(1,1))}")  # True
print(f"Adyacencias: {adjacent(X, Y, X1, Y1).data}")