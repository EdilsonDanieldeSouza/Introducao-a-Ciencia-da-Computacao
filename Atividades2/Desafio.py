import math

a = int(input('Digite o valor da letra A '))
b = int(input('Digite o valor da letra B '))
c = int(input('Digite o valor da letra C '))

resultado = (b ** 2) - 4 * a * c
if resultado > 0:
    y = math.sqrt((b ** 2) - 4 * a * c)
    raiz_um = (-b - y) / 2
    raiz_doiz = (-b + y) / 2
    print(f'As raizes da equação são {raiz_um} e {raiz_doiz}')
if resultado == 0:
    y = math.sqrt((b ** 2) - 4 * a * c)
    raiz_um = (-b - y) / 2
    raiz_doiz = (-b + y) / 2
    print('A raiz dessa equação é:', raiz_um)
if resultado < 0:
    print('Essa equação não possui raizes reais.')
