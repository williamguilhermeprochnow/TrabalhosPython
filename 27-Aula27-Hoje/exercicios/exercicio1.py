# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int

from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


# # 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# # f-string, responda as seguintes questões:


# # 1.1) Qual é o tamanho da lista1?


# # 1.2) Qual é o maior valor da lista2?


# # 1.3) Qual seria a soma do maior valor com o menor valor da lista2?


# # 1.4) Qual é a média aritmética da lista1?


# # 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# # quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)


# # 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.


# # 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# # trate para evitar o erro: IndexError


# # 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# # tamanho delas).


# # 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# # Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.


# # 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

#1
print(f"Tamanho da lista1 é igual: {len(lista1)} valor/es")
#2
print(f'O maior valor da lista2 é igual: {max(lista2)}')
#3
print(f'A soma entre esse dois número é igual: {max(lista2) + min(lista2)}')
#4
print(f'A média aritimética da lista1 é igual: {sum(lista1) / len(lista1)}')
#5
print(f'o resultado entra a soma da lista1 é igaual: {sum(lista1)} valor/es')
#
print(f'o resultado entra a soma da lista2 é igaual: {sum(lista2)} valor/es')
#
print(f'o resultado entra a soma da lista3 é igaual: {sum(lista3)} valor/es')
#
print(f'o resultado entra a soma de todas as listas é igual: {sum(lista1) + sum(lista2) + sum(lista3)} valor/es\n')
#6
for i in lista1:
    print(f'{i}')
print('\n')
#7
try:
    posicao = [5, 9, 10, 25]
    for ident in posicao:
        print(lista1[ident])

except IndexError as e:
    print(f'Posição {ident} não encontrada')
#8
if len(lista1) > len(lista2) and len(lista1) > len(lista3):
    print(f'\nLista1 com {len(lista1)} valor/es')
elif len(lista2) > len(lista3):
    print(f'\nLista2 com {len(lista2)} valor/es')
else:
    print(f'\nLista3 com {len(lista3)} valor/es')


#9
soma = (max(lista1) + max(lista2) + max(lista3))

def menores(lista1, lista2, lista3):
    if min(lista1) < min(lista2) and min(lista1) < min(lista3):
        print(f'\nO menor número é {min(lista1)}')
        menor_numero = min(lista1)
    elif min(lista2) < min(lista3):
        print(f'\nO menor número é {min(lista2)}')
        menor_numero = min(lista3)
    else:
        print(f'\nO menor número é {min(lista3)}')
        menor_numero = min(lista3)
    return menor_numero

menor_numero = menores(lista1, lista2, lista3)
subtracao = soma - menor_numero
print(soma)
print(subtracao)


#10
def maiores(lista1, lista2, lista3):
    if max(lista1) > max(lista2) and max(lista1) > max(lista3):
        print(f'\nO menor número é {max(lista1)}')
        maior_valor = max(lista1)
    elif max(lista2) > max(lista3):
        print(f'\nO menor número é {max(lista2)}')
        maior_valor = max(lista3)
    else:
        print(f'\nO menor número é {max(lista3)}')
        maior_valor = max(lista3)
    return maior_valor

def menor(lista1, lista2, lista3):
    if min(lista1) < min(lista2) and min(lista1) < min(lista3):
        print(f'\nO menor número é {min(lista1)}')
        menor_valor = min(lista1)
    elif min(lista2) < min(lista3):
        print(f'\nO menor número é {min(lista2)}')
        menor_valor = min(lista3)
    else:
        print(f'\nO menor número é {min(lista3)}')
        menor_valor = min(lista3)
    return menor_valor

maior_valor = maiores(lista1, lista2, lista3)
menor_valor = menor(lista1, lista2, lista3)
somatoria = maior_valor + menor_valor
print(somatoria)

# listas = [lista1, lista2, lista3]
# listas_len = []
# for lista in listas:
#     listas_len.append(len(lista))
# maior_lista = max(listas_len)

# print('A lista', listas_len.index(maior_lista)+1, 'é a maior')


# lista_len = [len(lista) for lista in listas]
# maior_lista = max(listas_len)
# lista_index = listas_len.index(maior_lista)+1
# print('A lista', listas_len.index(maior_lista)+1, 'é a maior')
