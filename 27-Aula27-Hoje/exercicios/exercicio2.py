# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).


# 2) Qual é o maior valor destas duas listas 


# 3) Qual é o maior valor de cada lista


# 4) Há o número 10 dentro da lista[0]?


# 5) Há o número 20 dentro da lista[1]?


# 6) Quantos números da lista[0] tem dentro da lista[1]?


# 7) Mostre os números da lista[0] que estão dentro da lista[1]


# 8) Mutliplique a soma da lista[0] com cada item da lista[1]


# 9) Faça uma divisão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!


# 10) verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]

#1
print(f'{lista is a and b}')

print(f'{lista == a and b}')


#2
print(f'Maior valor entre essas duas lista é: {max(lista[0 or 1])}')

#3
print(f'\nOs maiores valores de cada lista são: {max(lista[0])} lista0\n\t\t\t\t      {max(lista[1])} lista1')

#4
if 10 in lista[0]:
    print('SIM')
else:
    print('NÃO')

#5
if 20 in lista[1]:
    print('SIM')
else:
    print('NÃO')

#6
numeros_dentro = 0
for igual1 in lista[0]:
    for igual2 in lista[1]:
        if igual1 == igual2:
            numeros_dentro +=1
            print(f'Tem dentro da lista1: {numeros_dentro} números\n')
        else:
            print(f'Não tem números dentros...\n')

#7
numeros_iguais = 0
for igual1 in lista[0]:
    for igual2 in lista[1]:
        if igual1 == igual2:
            numeros_iguais = igual1 and igual2
            print(f'Tem em ambas as listas: {numeros_iguais}\n')
        else:
            print(f'Não tem números iguais...\n')

#8
soma = sum(lista[0])
for multi in lista[1]:
    print(f'{soma * multi}\n')

#9
maxint = max(lista[0 or 1])
print(maxint)
print('____')
minint = min(lista[0 or 1])
print(f'\n{minint}')
divisao_int = maxint // minint
print(divisao_int)


if divisao_int in lista[0]:
    print('O valor está na lista0.')
elif divisao_int in lista[1]:
    print('O valor está na lista1.')
else:
    print('O valor não está dentro de nunhuma destas listas.\n')

#10
maior_numero0 = max(lista[0])

if maior_numero0 in lista[1]:
    print('Esta aqui!!!\n')
else:
    print('Não está aqui. :(\n')

menor_numero1 = min(lista[1])

if menor_numero1 in lista[0]:
    print('Esta aqui!!!')
else:
    print('Não está aqui. :(')
