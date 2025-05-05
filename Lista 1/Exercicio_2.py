from sympy import symbols, integrate, sin, pi

# Definição da variável
x = symbols("x")

# a) ∫(3x² − 4x + 1) dx — integral indefinida
expr_a = 3 * x**2 - 4 * x + 1
int_a = integrate(expr_a, x)

# b) ∫₀^π sin(x) dx — integral definida
expr_b = sin(x)
int_b = integrate(expr_b, (x, 0, pi))

# c) ∫ 1 / (x² + 1) dx — integral indefinida
expr_c = 1 / (x**2 + 1)
int_c = integrate(expr_c, x)

# Exibindo os resultados
print("a) ∫(3x² − 4x + 1) dx =", int_a)
print("b) ∫₀^π sin(x) dx =", int_b)
print("c) ∫ 1 / (x² + 1) dx =", int_c)
