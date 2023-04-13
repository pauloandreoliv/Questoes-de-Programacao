#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#O menor valor de faturamento ocorrido em um dia do mês;
#O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('dados.json') as arquivo:
    dados = json.load(arquivo)

total_dias = len(dados)

soma = 0
dias_sem_fat = 0
menor = 0
maior = 0

tem_zero = False

cont = 0
while cont < total_dias:

    valor = dados[cont]['valor']
    
    soma += valor

    if menor == 0 and tem_zero is not True:
        menor = valor
    if menor != 0 and menor > valor:
        menor = valor
    if valor == 0:
        menor = 0
        tem_zero = True
        dias_sem_fat += 1
    if valor > maior:
        maior = valor
    cont +=1

media = soma/(total_dias - dias_sem_fat)
dias_sup_media = 0

cont_media = 0
while cont_media < total_dias:

    valor = dados[cont_media]['valor']
    
    if valor > media:
        dias_sup_media +=1
    
    cont_media += 1

print("Menor faturamento do mês: " + str(menor))
print("Maior faturamento do mês: " + str(maior))
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: " + str(dias_sup_media))
