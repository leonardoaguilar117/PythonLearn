# A way to order and filter lists are compression lists, these are used to sorted or classificate
# lists with especific parameters

list_A = [
    ["Nombre:", "Emiliano"],
    ["Nombre:", "Josue"],
    ["Nombre:", "Victor"]
]

# Non usual way
for names in list_A:
    print(names[1])

# Compression list
# Syntax: variable = [expresion for item in items
names = [names[1] for names in list_A]
print(names)

# Compression list with condition
names_2 = [names[1] for names in list_A if names[1] == "Josue"]
print(names_2)
