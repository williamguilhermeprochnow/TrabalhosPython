# Aula 18 - 03-11-2019

# A lista a seguir possui mais uma lista interna, a lista de preços.
# A lista de preços possui 3 sublistas dentro dela com os preços dos produtos.
# para exemplificar, o preço do mamão é de 10.00 - alface crespa é de 2.99 e o feijão 9.0

lista = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5], [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] ]
        ]

# Será solicitado o preço de alguns produtos. para imprimir deve ser por f-string refrenciando o nome com o preço 
# da seguinte forma: "O preço do {} é R$ {}"

print('1: imprima o valor do abacaxi')

print(f'O preço do {lista[1][1]} é R${lista[4][0][1]}')

print('2: imprima o valor da rucula')

print(f'O preço da {lista[2][2]} é R${lista[4][1][2]}')

print('3: imprima o valor da laranja')

print(f'O preço da {lista[1][2]} é R${lista[4][0][2]}')

print('4: imprima o valor do repolho')

print(f'O preço do {lista[2][4]} é R${lista[4][1][4]}')

print('5: imprima o valor do feijão')

print(f'O preço do {lista[3][0]} é R${lista[4][2][0]}')

print('6: imprima o valor do feijão branco')

print(f'O preço do {lista[3][4]} é R${lista[4][2][4]}')

print('7: imprima o valor da vergamota')

print(f'O preço da {lista[1][6]} é R${lista[4][0][6]}')

print('8: imprima o valor da alface lisa')

print(f'O preço da {lista[2][1]} é R${lista[4][1][1]}')

print('9: imprima o valor do mamão')

print(f'O preço da {lista[1][0]} é R${lista[4][1][2]}')

print('10: imprima o valor da soja')

print(f'O preço da {lista[3][6]} é R${lista[4][2][6]}')

print('11: imprima o valor da lentilha')

print(f'O preço da {lista[3][2]} é R${lista[4][2][2]}')

print('12: imprima o valor da uva')

print(f'O preço da {lista[1][3]} é R${lista[4][0][3]}')

print('13: imprima o valor da vagem')

print(f'O preço da {lista[3][3]} é R${lista[4][2][3]}')

print('14: imprima o valor do almeirão')

print(f'O preço da {lista[2][4]} é R${lista[4][1][3]}')

print('15: imprima o valor da ervilha')

print(f'O preço da {lista[3][1]} é R${lista[4][2][1]}')

print('16: imprima o valor da maçã')

print(f'O preço da {lista[1][5]} é R${lista[4][0][5]}')