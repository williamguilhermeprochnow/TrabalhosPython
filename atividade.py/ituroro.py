('='*50)
numero = int(input('0 - Sair\n1 - Cadastrar\n2 - Listar\nOpção inválida\nO que desejas fazer: '))
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