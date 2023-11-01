# it´s like a list but inmutable
tuple = (1, 2, 44) + (-1, -44, 4)
print(tuple)

setOne = {1, 4, 6, -33, 0, -2}
setTwo = {3, 5, 11, 4, -2, -10}

print(setOne | setTwo)  # union
print(setOne & setTwo)  # intersection
print(setOne - setTwo)  # Difference
