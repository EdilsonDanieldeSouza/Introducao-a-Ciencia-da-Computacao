import math

a = float(input('Digite o valor da letra A '))
b = float(input('Digite o valor da letra B '))
c = float(input('Digite o valor da letra C '))

delta = (b ** 2) - 4 * a * c
if delta > 0:
    y = math.sqrt((b ** 2) - 4 * a * c)
    raiz_um = (-b - y) / 2
    raiz_dois = (-b + y) / 2
    print(f'As raizes da equação são {raiz_um} e {raiz_dois}')
if delta == 0:
    y = math.sqrt((b ** 2) - 4 * a * c)
    raiz_um = (-b - y) / 2
    raiz_dois = (-b + y) / 2
    print('A raiz dessa equação é:', raiz_um)
if delta < 0:
    print('Essa equação não possui raizes reais.')
