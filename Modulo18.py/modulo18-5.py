#--- Exercício 5 - Funções - 2
#--- Crie uma função que valida um menu
#--- A função deve receber um número inteiro
#--- A função deve checar se o número está entre 0 e 2
#--- Caso o número esteja fora deste range deve ser informado 'Opção inválida'
#--- Caso o número informado esteja dentro do range deve seguir as seguintes regras:
#---    0-Chamar uma função Sair(), esta função deve imprimir 'Usuário realizou o logoff'
#---    1-Chamar uma função Cadastrar(), esta função deve imprimir 'Cadastro de usuários'
#---    2-Chamar uma função Listar(), esta função deve imprimir 'Lista de usuários cadastrados'
#--- Crie um menu com cabeçalho e rodapé com as opções listadas acima
#--- Realize a leitura da opção digitada pelo usuário no terminal
#--- Realize a chamada da função que valida o menu e passe o variável criada durante a leitura do terminal

numero = int(input('0 - Sair\n1 - Cadastrar\n2 - Listar\nOpção inválida\nDigie o numero: '))
def menu(numero):
    if numero == 0:
        print('Usuário realizou o logoff')
    elif numero == 1:
        print('Cadastro de usuários')
    elif numero == 2:
        print('Lista de usuários cadastrados')
    else:
        print('Opção invalida')
    return numero
menu(numero)

