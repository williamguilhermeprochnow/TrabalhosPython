# Faça um programa que leia um número inteiro de 1 a 10 no teclado e mostre se você acertou, o número digitado é maior ou menor.
# Quando você acertar o programa deve ser finalizado

from random import randint
aleatorio = randint(1,10)
# --->>>print(aleatorio)
numero = 0
#ni = int(input('Digite algum número inteiro: '))

while not numero == aleatorio:
    numero = int(input('Digite o número inteiro: '))
    if numero < aleatorio:
        print('O número é maior!')
    elif numero > aleatorio:
        print('O número é menor!')
    else:
        print('Você acertou!!!')
