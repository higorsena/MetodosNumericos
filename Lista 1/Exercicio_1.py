from sympy import symbols, diff, exp, sin, ln

# Definição das variáveis
x = symbols("x")
t = symbols("t")
y = symbols("y")

# a) f(x) = x^3 + 2x^2 - 5x + 1
f = x**3 + 2 * x**2 - 5 * x + 1
df_dx = diff(f, x)

# b) g(t) = e^(2t) * sin(t)
g = exp(2 * t) * sin(t)
dg_dt = diff(g, t)

# c) h(y) = ln(y^2 + 1)
h = ln(y**2 + 1)
dh_dy = diff(h, y)

# Exibindo os resultados
print("f'(x) =", df_dx)
print("g'(t) =", dg_dt)
print("h'(y) =", dh_dy)
