#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

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
