from sympy import symbols, expand, S

# Define la variable
x = symbols('x')

# Tu expresión (por ejemplo)
expresion = (x**(1/2) + 2*x**(3/4) + x**2)

# Expande la expresión si es necesario
expresion_expandida = expand(expresion)

# Obtiene el diccionario de coeficientes
coeficientes = expresion_expandida.as_coefficients_dict()

# Inicializa un diccionario para almacenar los coeficientes fraccionarios
coeficientes_fraccionarios = {}

# Itera sobre los términos y obtén los exponentes de 'x'
for x_term, coef in coeficientes.items():
    exponente = x_term.as_poly().degree()
    exponente_sympy = S(exponente)  # Convierte el exponente a un objeto Sympy
    if exponente_sympy.is_rational:
        coeficientes_fraccionarios[exponente_sympy] = coef

# Muestra los coeficientes fraccionarios
print("Coeficientes fraccionarios:")
for exponente, coef in coeficientes_fraccionarios.items():
    print(f"Exponente {exponente}: Coeficiente {coef}")
