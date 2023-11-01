orden = [
    ["Character", 1],
    ["First", 2],
    ["Desmond", 3]
]


def showList(list):
    for elements in list:
        print(elements)

# Lambda syntax is a simple convention to write a function,
# these are better when we need use once a function


def cuadrado(x): return x**2


resultado = cuadrado(4)
print(resultado)  # Resultado: 16

showList(orden)
