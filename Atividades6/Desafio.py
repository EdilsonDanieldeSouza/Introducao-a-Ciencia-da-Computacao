n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def numero_binominal(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

print(numero_binominal(n, k))
