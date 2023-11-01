import math

# A = base, B = exponente n = operador de modular


def ExponenciacionBinaria(a, b, n):
    expontenteBin = bin(b)[2:]

    for i in range(len(expontenteBin) - 1, -1, -1):  # para
        Resultado = (int(expontenteBin[i])**2) % n

        if int(expontenteBin[i]) == 1:
            Resultado = (Resultado * a) % n

    return Resultado


print(ExponenciacionBinaria(5, 3, 17))
