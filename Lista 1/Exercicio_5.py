def intervalo_soma(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def intervalo_produto(a, b):
    produtos = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return [min(produtos), max(produtos)]


def intervalo_divisao(a, b):
    if 0 in b:
        raise ValueError("Divisão por intervalo contendo zero não é permitida.")
    divs = [a[0] / b[0], a[0] / b[1], a[1] / b[0], a[1] / b[1]]
    return [min(divs), max(divs)]


# Intervalos do exercício 5
x = [0.99, 1.01]
y = [1.98, 2.02]

# Cálculos
soma = intervalo_soma(x, y)
produto = intervalo_produto(x, y)
divisao = intervalo_divisao(x, y)

print(f"x + y = {soma}")
print(f"x · y = {produto}")
print(f"x / y = {divisao}")
