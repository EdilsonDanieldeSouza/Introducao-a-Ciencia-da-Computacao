 # potencia
i = 1
while i < 50:
    print(2 ** i)
    i += 1

# soma
inicia = 0
quantidade = int(input('Quantos números você quer somar? '))
soma = 0
while inicia < quantidade:
    valor = int(input('Digite o valor a ser somado '))
    soma += valor
    inicia += 1

print('A soma dos valores digitados é:', soma)

# produto
inicia = 0
quantidade = int(input('Quantos números você quer multiplicar? '))
produto = 1
while inicia < quantidade:
    valor = int(input('Digite o valor a ser multiplicado '))
    produto *= valor
    inicia += 1

print('O produto dos valores digitados é:', produto)

# soma do numeros de um valor com varias casas decimais
