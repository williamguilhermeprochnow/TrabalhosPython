# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.

#>1 e 2
controle = 'n'
while controle != 's':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    print(f'A soma entre esses dois números é igual: {n1 + n2}')
    print(f'A multiplicação entre esses dois números é igual: {n1 * n2}')
    print(f'A divisão entre esses dois números é igual: {n1 / n2}')
    print(f'A subtração entre esses dois números é igual: {n1 - n2}')

    controle = input('Digite "s" para sair: ')

#>3
while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        print(f'A soma entre esses dois números é igual: {n1 + n2}')
        print(f'A multiplicação entre esses dois números é igual: {n1 * n2}')
        print(f'A divisão entre esses dois números é igual: {n1 / n2}')
        print(f'A subtração entre esses dois números é igual: {n1 - n2}')

    except ValueError:
        print('Por favor digite um valor inteiro para o procedimento continuar!')
    else:
        print('Acerto Mizeravi')
        break

#>4
while True:
    try:
        print('Passou 1')
        numero = int(input('Digite um numero1:'))
        numero2 = int(input('Digite um numero2:'))

        print(numero/numero2)
        print('Passou 2')

    except (ValueError,ZeroDivisionError):
        print('Voce digitou ALGO errado CEU!!! animaUUU!')

    # except ZeroDivisionError:
    #     print('Voce dividiu por zero')

    else:
        print('FIM!')
        break

###############################################################################################

# try:
#    numero = int(input('Digite um número: '))

# except:
#     print('Você digitou o número errado animal!')

# print('1')
# print('2')

# while True:
#     try:
#         n = 0
#        while True:
#           print(n)
#           n+=1
#     except:
#         print('Ferrou!')

# while True:
#     try:
#         print('Passou 1')
#         numero = int(input('Digite um número: '))
#         print('Passou 2')
    
#     except ValueError:
    
#         print('Você digitou o número errado animal!')
    
#     else:
#         print('Fim!')
#         break