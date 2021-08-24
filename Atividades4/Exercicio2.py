import math

a = float(input('Digite o valor da letra A '))
b = float(input('Digite o valor da letra B '))
c = float(input('Digite o valor da letra C '))

delta = (b ** 2) - 4 * a * c
if delta > 0:
    y = math.sqrt((b ** 2) - 4 * a * c)
    raiz_um = (-b - y) / 2
    raiz_dois = (-b + y) / 2
    if raiz_um < raiz_dois:
        print(f'As raízes da equação são {raiz_um} e {raiz_dois}')
    else:
        print(f'As raízes da equação são {raiz_dois} e {raiz_um}')
if delta == 0:
    y = math.sqrt((b ** 2) - 4 * a * c)
    raiz = (-b - y) / 2
    print('A raiz dupla desta equação é', raiz)
if delta < 0:
    print('Está equação não possui raízes reais')
