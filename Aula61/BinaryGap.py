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


def con(n):
    # n = bin(N)
    # n = '0b000000101001000100001'
    lista = list(n)
    lista.remove(lista[0])
    lista.remove(lista[0])
    print(lista)
    contador = 0
    ultimo = 0
    maior = 0
    for i in lista:
        if i == '0' and ultimo == '0':
            contador += 1
        elif i == '0' and ultimo == '1':
            contador =1
        elif i != '0':
            if contador > maior:
                maior = contador

        ultimo = i
    return maior




assert con('0b00000010100100010000100000') == 4 , f"erro: O resultado foi {con('0b00000010100100010000100000')} e deveria ser o número 4"
print("O resultado foi perfeito")