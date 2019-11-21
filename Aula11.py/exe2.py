from calc2 import *

valor = float(input('\nDigite o valor que será poupado:'))
rent = float(input('\nDigite a rentabilidade:'))

valor_mes = calcmes(valor, rent)
valor_ano = calc_ano(valor, rent)

pritn(f'\nA rentabilidade aplicada foi de: {rent}')