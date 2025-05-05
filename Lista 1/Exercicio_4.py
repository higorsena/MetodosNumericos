from sympy import Interval, Min, Max, Rational

# Definindo os intervalos
A = Interval(1, 2)
B = Interval(3, 5)

# a) Soma: [a1 + b1, a2 + b2]
sum_interval = Interval(A.start + B.start, A.end + B.end)

# b) Produto: [min(a*b), max(a*b)]
products = [A.start * B.start, A.start * B.end, A.end * B.start, A.end * B.end]
product_interval = Interval(Min(*products), Max(*products))

# c) Divisão: [min(a/b), max(a/b)]
divisions = [A.start / B.start, A.start / B.end, A.end / B.start, A.end / B.end]
division_interval = Interval(Min(*divisions), Max(*divisions))

# d) Subtração: [a1 - b2, a2 - b1]
subtraction_interval = Interval(A.start - B.end, A.end - B.start)

# Exibindo os resultados
print("a) A + B =", sum_interval)
print("b) A · B =", product_interval)
print("c) A / B =", division_interval)
print("d) A - B =", subtraction_interval)
