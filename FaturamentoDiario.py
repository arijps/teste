import json

f = open('faturamento.json')

fatur = json.load(f)

aux = 0
maior = 0
menor = 0
soma = 0
media = 0

for dia in fatur:

    if (dia['valor']) != 0:
        aux = dia['valor']
        if (aux > maior):
            maior = aux

        if (menor == 0):
            menor = aux
        elif (aux < menor):
            menor = aux

            soma += dia['valor']

print('O maior faturamento no mês foi de: R$ ' + str(maior) + '.')
print('O menor faturamento no mês foi de: R$ ' + str(menor) + '.')

media = soma / len(fatur)

diasFaturamento = ''

for i in fatur:
    if (i['valor']) != 0:
            if (i['valor']) > media:
                diasFaturamento += (str(i['dia']) + ' ')

print('Os dias em que o faturamento foi maior que a média mensal foram: ' + diasFaturamento)