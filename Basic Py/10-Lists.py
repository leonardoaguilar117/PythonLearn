# The arrays don´t exists in python, what exists are lists
# Lists are a colection of data whith similar structure that arrays, but have a difference
# has you can save different types of variables
# Slide convention is the easy way to cut a list, with this, we could make a new list with specific elements

listOne = [1234, 54767, 35532, 43678, 34578]
listTree = ["x", "y", "z"]
print(listOne[:1])
print(listOne[0::3])
print(listOne[3:])

# Make a list that has a numeration since 1 at 30
listTwo = list(range(1, 31))
print(listTwo)

# A way to unpack items to variables
A, B, C = listTree
print(A, B, C)

# Iterate elements inside list
elements = ["X", "Y", "Z", "W"]
for item in elements:
    print(item)

# This way only show items inside a list, to show a index assigned each, we use this syntax
for i, item in enumerate(elements):
    print(i, item)

# We suposed that have a list named pets and we add, delete and change pets inside
pets = ["Dog", "Cat", "Capybara"]

pets.insert(3, "Elephant")
print(pets)
pets.append("Cammel")
print(pets)
pets.pop(0)
print(pets)

# Unpack operator with list
list1 = [1, 2, 3, 4, 5, 6]
list2 = [57, 16, -1]

listUnpack = [*list1, *list2]

# Unpack operator with dictionaries
dictA = {
    "X": 45,
    "Y": 21
}

dictB = {
    "X": 33,
    "Y": 11
}

dictUnpack = {**dictA, **dictB}
