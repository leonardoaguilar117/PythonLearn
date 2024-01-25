# Importamos las librerias necesarias
import re
import sympy as sp
from sympy.abc import t

# Definimos la funcion principal
mainEquation = "(d(x))/(3*sen(x)+4*cos(x))"

# En un diccionario asignamos los valores que tendrá cada cambio de variable
values = {
    "d(x)": "2 / (1 + t**2)",
    "sen(x)": "2 * t / (1 + t**2)",
    "cos(x)": "(1 - t**2) / (1 + t**2)"
}

# Funcion que nos permite iterar cada elemento de values y cambiar los valores que encuentre
firstSubstution = re.compile('|'.join(map(re.escape, values.keys())))


def reemplazar(match):
    return values[match.group(0)]


# En eqInT hacemos la primera sustitución, es decir, cambiaremos los valores de mainEquation por values
eqInT = firstSubstution.sub(reemplazar, mainEquation)

# Transformamos a un objeto de tipo sympy para integrar
equation = sp.sympify(eqInT)

# Mostramos la func principal, el resultado con cambio de variable y el resultado de la integral
print("Función principal: ", mainEquation)
print("Primera sustitución: ", eqInT)
tIntegrate = sp.integrate(equation, t)
print("Resultado integración: ", tIntegrate)
tIntegrateSympObj = str(tIntegrate)

# Volvemos a sustituir pero en este caso todas las t en el cambio de variable
secondSubstitution = re.sub('t', 'tan(x/2)', tIntegrateSympObj)
print("Segunda sustitución y resultado final: ", secondSubstitution)
