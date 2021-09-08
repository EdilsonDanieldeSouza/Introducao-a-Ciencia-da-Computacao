from math import factorial

n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))


def fatorial(numero):
    return factorial(numero)


CoefBiominal = fatorial(n) / factorial(k) * factorial(n - k)
print(CoefBiominal)