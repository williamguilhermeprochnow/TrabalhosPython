#--- Exercício 2 - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, posicao, Numero, Perna boa
#--- Crie um dicionario para armazenar os dados
#--- Imprima todos os jogadores e seus dados

#dicionario_jogadores = {'Nome':'', 'Posicao':'', 'Numero':'', 'Perna boa':''}
lista_jogadores = []
for i in range(1,11):
    dicionario_jogadores = {}
    dicionario_jogadores['Nome'] = input('Digite o Nome:')
    dicionario_jogadores['Posicao'] = input('Digite a Posicao:')
    dicionario_jogadores['Numero'] = int(input('Digite o Numero:'))
    dicionario_jogadores['Perna_boa'] = input('Digite a Perna boa:')
    lista_jogadores.append(dicionario_jogadores)

for i in lista_jogadores:
    print(i['Nome'], i['posicao'], i['Numero'], i['Perna_boa'])