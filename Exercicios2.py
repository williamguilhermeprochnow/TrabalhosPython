#--- Exercício 2 - for
#--- Escreva programa que leia um numero inteiro
#--- Calacule a taboada do número informado
#--- Imprima a taboada com a conta completa (n*i=r)

lisNI = int(input('Digite o numero:'))


for i in range (0,11):
    print(f'{i} x {lisNI} = {i*lisNI}')