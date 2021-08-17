numero = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = numero // 86400
diasSobra = numero % 86400
horas = diasSobra // 3600
horasSobra = diasSobra % 3600
minutos = horasSobra // 60
segundos = horasSobra % 60


print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')