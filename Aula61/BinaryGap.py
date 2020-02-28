# Um espaço binário dentro de um número inteiro positivo N é qualquer sequência máxima de zeros consecutivos
# que está rodeado por 1 dos dois lados na representação binária de N.
#
# Por exemplo, o número 9 tem representação binária 1001 e contém uma lacuna binária de comprimento 2.
# O número 529 tem representação binária 1000010001 e contém duas lacunas binárias:
# um de comprimento 4 e um de comprimento 3.
# O número 20 tem representação binária 10100 e contém um espaço binário de comprimento 1.
# O número 15 tem representação binária 1111 e não possui lacunas binárias.
# O número 32 tem representação binária 100000 e não possui lacunas binárias.
#
# Escreva uma função:
#
# solução def (N)
#
# que, dado um número inteiro positivo N, retorna o comprimento de seu maior intervalo binário.
# A função deve retornar 0 se N não contiver um espaço binário.
#
# Exemplo, dado N = 1041, a função deve retornar 5,
# porque N tem representação binária 10000010001 e, portanto, seu maior intervalo binário tem o comprimento 5.
#
# Dado N = 32, a função deve retornar 0, porque N tem representação binária '100000'
# e, portanto, sem lacunas binárias.

# N = int(input('Digite o número: '))

def convertendo(numero_natural):
    numero_natural_em_bin = bin(numero_natural)
    binario = numero_natural_em_bin[2:]
    return binario

def contando_os_espacos_binarios(binario):
    lista_com_zeros = binario.split('1') # Lista só com zeros
    max_zero_na_lista = len(max(lista_com_zeros))
    menssagem = f'o maior intervalo binário de {binario} é {max_zero_na_lista}'
    return print(menssagem)

x = convertendo(2)
contando_os_espacos_binarios(x)