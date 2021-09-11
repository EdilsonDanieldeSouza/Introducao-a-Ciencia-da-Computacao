def maior_primo(numero):
    num = numero
    contador = 0
    i = 0
    if numero >= 2:
        f = False
        while f == False:
            while i <= num or contador < 2:
                i += 1
                RestDiv = num % i
                if RestDiv == 0:
                    contador = contador + 1
            if contador <= 2:
                f = True
            else:
                num -= 1
                i = contador = 0
        return num