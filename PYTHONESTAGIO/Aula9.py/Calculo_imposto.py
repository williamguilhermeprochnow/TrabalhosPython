# Aula 9 - 19-11-2019
#--- Método

print('='*50, '\n')

salario = float(input('Digite seu salario:'))

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)

salario_liquido = salario - inss - irrf
print(f'INSS: {inss}')
print(f'IRRF: {irrf}')
print(f'Seu salário liquido é {salario_liquido}')

print('\n'*2, '=',50)

# def calculo_inss(salario):
#     if(salario>0 and salario <=1751.81):
#         inss = salario * 0.08
#     elif (salario > 1751.81 and salario <= 2919.72 ):
#         inss = salario * 0.090
#     elif (salario >2919.72 and salario<=5839.45 ):
#         inss = salario * 0.11
#     else:
#         inss = 642.34
#     return inss

# print('='*50, '\n')

# valor = float(input('Digite seu salario:'))

# imposto = calculo_inss(salario)

# def calculo_inss(salario, inss):
#     if(salario>1903.98 and salario <=2826.65):
#         irrf = (((salario - inss) * 0.075)-0.0
#     elif (salario > 1751.81 and salario <= 2919.72 ):
#         inss = salario * 0.090
#     elif (salario >2919.72 and salario<=5839.45 ):
#         inss = salario * 0.11
#     else:
#         inss = 642.34
#     return irrf

#     salario = float((input))

from calculo_imposto import calculo_inss, calculo_irrf


print('='*50, '\n')

salario = float( input('Digite seu salario:') )

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)

salario_liquido = salario - inss - irrf
print(f'Inss: {inss}')
print(f'Irrf: {irrf}')
print(f'Seu salário liquido é {salario_liquido}')

print( '\n'*2,'='*50)



# nome_completo = input('Digite seu nome completo:')
# cpf = input('Digite seu cpf:')
# num_registro = int( input('Digite seu registro:') )
# cargo = input('Digite seu cargo:')