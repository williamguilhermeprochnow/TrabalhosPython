# 1- Faça um menu interativo que tenha: Cadastro da banda, Cadastro do album, cadastro da música, Sair.
# O menu ser executado até que se escolha a opção sair.
# Cada opção deve ser mostrada quando selcionado a opção sair, deverá aparecer na tela as informações das bandas cadastradas, albuns e músicas.

# cadastro = int(input('0 - Sair\n1 - Cadastro da banda\n2 - Cadastro do album\nOpção inválida\nDigie a opção de acordo com os números: '))
# #def menu(cadastro):
# while True:(cadastro)
#     cadastramento = input(cadastro)
#     if numero == 0:
#         print('Cancelar cadastramento')
#     elif numero == 1:
#         print(input('Cadastro da banda: '))
#     elif numero == 2:
#         print(input('Cadastro do album'))
#     else:
#         print('Opção invalida')
#     return numero
# menu(cadastro)

lista_bandas = []
lista_album = []
lista_musica = []

menu = '''
1- Cadastro da banda
2- Cadastro do album
3- Cadastro da música
4- Sair

Digite a opção: '''



while True:
    opcao = input(menu)
    if opcao == '1':
        lista_bandas.append(input('Digite o nome banda: '))
    elif opcao =='2':
        lista_bandas.append(input('Digite o nome do album: '))
    elif opcao == '3':
        lista_bandas.append(input('Digite o nome da música: '))
    elif opcao == '4':
        print(f'Lista das bandas: {lista_bandas}\nLista dos albuns: {lista_album}\nLista das musicas: ')
        break
    else:
        print('Opção inválida')

