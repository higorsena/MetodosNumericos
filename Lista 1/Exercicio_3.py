from sympy import symbols, Function, Eq, dsolve, exp

# Definindo variáveis
x = symbols("x")
y = Function("y")

# a) dy/dx = 3x^2
eq_a = Eq(y(x).diff(x), 3 * x**2)
sol_a = dsolve(eq_a, y(x))

# b) dy/dx + y = e^x
eq_b = Eq(y(x).diff(x) + y(x), exp(x))
sol_b = dsolve(eq_b, y(x))

# Exibindo os resultados
print("a) Solução da EDO dy/dx = 3x² →", sol_a)
print("b) Solução da EDO dy/dx + y = e^x →", sol_b)
