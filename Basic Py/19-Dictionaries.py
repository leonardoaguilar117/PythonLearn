# each element have one item assigned
dictoOne = {
    "x": 25,
    "y": 32,
    "w": 23
}

# add element to dictoOne
dictoOne["z"] = 34

# shows items assigned
for element in dictoOne:
    print(dictoOne[element])

# print a element
print(dictoOne.get("x"))

# delete one element
del dictoOne["x"]

# delete item assigned to element
del (dictoOne["y"])
print(dictoOne.get("y"))

# dictionary with sets
users = [
    {"id": 23},
    {"id": 44},
    {"id": 1}
]

for ages in users:
    print(f"age: {ages['id']}")
