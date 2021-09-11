import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input('Digite o valor da letra A '))
    b = float(input('Digite o valor da letra B '))
    c = float(input('Digite o valor da letra C '))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print('A única raiz é: ', raiz1)
    else:
        if d < 0:
            print('Esta equação não possui raizes reais')
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print('A primeira raiz é; ', raiz1)
            print('A segunda raiz é ', raiz2)
main()