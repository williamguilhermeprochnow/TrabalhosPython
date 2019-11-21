# Aula 11 - 21-11-2019
# Exercícios

#1--- Crie um programa que calcule o imposto ISS de um serviço de desenvolvimento de software - utilizar metodos
#2--- Calcule a rentabilidade anual de um investimento baseando-se em sua rentabilidade mensal (juros composto) 
# a rentabilidade deve ser apresentada em % e R$ - utilizar metodos
#3--- Crie um programa para calculo de numeros de cotas 
#     solicitar valor a ser investido no tesouro selic
#     (Considerar o valor do tesouro selic hoje)
#     calcular o valor total até o vencimento do titulo
#    -utilizar metodos
#4--- 
#5--- 
# preço unitário: 10.410.00 vencimento: 01/03/2025
from calculo_imposto import calculo_iss
print('='*50, '\n')

salario = float( input('Digite seu salario:') )

iss = calculo_iss(salario)

salario_liquido = salario - iss
print(f'Iss: {iss}')
print(f'Seu salário liquido é {salario_liquido}')

print( '\n'*1,'='*50)






