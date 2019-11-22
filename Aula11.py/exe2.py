from calc2 import *

valor = float(input('\nDigite o valor que será poupado:'))
rent = float(input('\nDigite a rentabilidade:'))

valor_mes = calc_mes(valor, rent)
valor_ano = calc_ano(valor, rent)

print(f'''\nA rentabilidade aplicada foi de: {rent*100}% \n O lucro por mês será de: {valor_mes} \nO lucro por ano será de: {valor_ano:0.2f}\n''') 
