import json

with open("dados.json", encoding='utf-8') as arq_json:
    dados = json.load(arq_json)

menor_valor = ''
maior_valor = ''
dia_maior = ''
dia_menor = ''
cont = 1
soma = 0
dias_acima_media = 0
contador_dia_faturado = 0

for c in dados:
    if cont == 1:
        menor_valor = c["valor"]
        dia_menor = c["dia"]
        maior_valor = c["valor"]
        dia_maior = c["dia"]

    elif c["valor"] < menor_valor and c["valor"] != 0:
        menor_valor = c["valor"]
        dia_menor = c["dia"]

    elif c["valor"] > maior_valor:
        maior_valor = c["valor"]
        dia_maior = c["dia"]
    cont += 1

for c in dados:
    soma = soma + c["valor"]
    if c["valor"] != 0:
        contador_dia_faturado += 1

media = soma / contador_dia_faturado

for c in dados:
    if c["valor"] > media:
        dias_acima_media += 1

print(f'O maior valor de faturamento ocorrido em um dia do mês foi de {maior_valor:.2f} no dia {dia_maior}.')
print(f'O menor valor de faturamento ocorrido em um dia do mês foi de {menor_valor:.2f} no dia {dia_menor}.')
print(f'Em {dias_acima_media} dias o faturamento diário foi maior que a média mensal.')
