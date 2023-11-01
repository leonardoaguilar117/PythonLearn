"""Simple array rotation"""


def solve(opc, array):
    arrayAUX = []
    if opc == "A":
        return array
    elif opc == "RA":
        return solveRA(array)
    elif opc == "D":
        return solveD(array)
    elif opc == "RD":
        return solveD(solveRA(array))


def solveRA(array):
    arrayAUX = []
    for i in range(0, len(array)):
        if i == 0:
            arrayAUX.insert(0, (array[-1]))
        arrayAUX.append(array[i])
    del arrayAUX[-1]
    return arrayAUX


def solveD(array):
    arrayAUX = []
    tam = len(array)-1
    for i in range(tam, -1, -1):
        arrayAUX.append(array[i])
    return arrayAUX


list_1 = [1, 2, 3, 4, 8, 10, 14]
print(solve("A", list_1))
print(solve("RA", list_1))
print(solve("D", list_1))
print(solve("RD", list_1))
