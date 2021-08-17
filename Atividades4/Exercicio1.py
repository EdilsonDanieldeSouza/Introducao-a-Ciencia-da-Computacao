import math
numero1 = int(input('Dígite a coordenadas x: '))
numero2 = int(input('Dígite coordenadas y: '))
numero3 = int(input('Dígite coordenadas x: '))
numero4 = int(input('Dígitw coordenadas y: '))

distancia = math.sqrt(((numero1 - numero3) ** 2) + ((numero2 - numero4) ** 2))

if distancia >= 10:
    print('longe')
else:
    print('perto')