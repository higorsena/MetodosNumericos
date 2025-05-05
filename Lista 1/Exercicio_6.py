import math

# Intervalo de a
a = [0.999, 1.001]

# Etapa a: usar matemática intervalar para f(a) = sin(a^2)
a_squared = [
    a[0] ** 2,
    a[1] ** 2,
]  # quadrado do intervalo (como está todo positivo, basta elevar extremos)
f_a_interval = [math.sin(a_squared[0]), math.sin(a_squared[1])]
intervalo_estimado = [min(f_a_interval), max(f_a_interval)]

# Etapa b: valor no ponto médio
a_meio = (a[0] + a[1]) / 2
f_meio = math.sin(a_meio**2)

print(f"Intervalo estimado de f(a) = sin(a^2): {intervalo_estimado}")
print(f"Avaliação em ponto médio f(1.0): {f_meio}")
