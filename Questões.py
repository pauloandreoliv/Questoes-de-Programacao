#1)
'''INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)'''

#2)

lista = [0,1]

numero = int(input("Insira o número desejado: "))

k = 1
valor = 0
while valor < numero and k != len(lista):
    pos_anterior = k - 1
    valor = lista[k] + lista[pos_anterior]
    lista.append(valor)
    k+=1
    
if numero in lista:
    print(numero + " está na sequência de Fibonacci")
else:
    print(numero + " não está na sequência de Fibonacci")
