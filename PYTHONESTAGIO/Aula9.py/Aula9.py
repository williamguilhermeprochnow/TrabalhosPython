# Aula 9 - 19-11-2019
#--- Crie um programa que:
#--- 1- Leia dois números inteiros
#--- 2- Clcule a soma entre os dois numeros atraves de um metodo
#--- 3- Clcule a subtração entre os dois numeros atraves de um metodo
#--- 4- Clcule a multiplicação entre os dois numeros atraves de um metodo
#--- 5- Clcule a divisão inteira entre os dois numeros atraves de um metodo
#--- 6- Clcule a divisão fracionada entre os dois numeros atraves de um metodo
#--- 7- Clcule o resto da divisão entre os dois numeros atraves de um metodo
#--- 8- Clcule a raiz entre os dois numeros atraves de um metodo
#--- 9- Separa os metodos em outro arquivo

#1
#9
from pasta_importação import soma, subtracao, multiplicacao, divisaoi, divisaof, restod, raiz

ni = int(input('Digite o numero inteiro:'))
ni2 = int(input('Digite outro número inteiro:'))

#2
print(f'A soma :{soma(ni,ni2)}')

#3
print(f'A subtração :{subtracao(ni,ni2)}')

##4
print(f'A multiplicação :{multiplicacao(ni,ni2)}')

#5
print(f'A divisão inteiro :{divisaoi(ni,ni2)}')

#6
print(f'A divisão fracionada :{divisaof(ni,ni2)}')

#7
print(f'O resta da divisão :{restod(ni,ni2)}')

#8
print(f'A raiz :{raiz(ni,ni2)}')
