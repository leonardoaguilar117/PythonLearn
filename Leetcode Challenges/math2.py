import sympy as sp
import math
from sympy.abc import x, z


def excercise2(exp, function):
    mcm = math.lcm(*exp)
    dx = mcm * z ** (mcm-1)

    print("Funcion inicial: ")
    display(function)

    function = function.subs(x, z**mcm) * dx
    print()
