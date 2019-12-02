# 1--- o programa deve conter um menu interativo com cabeçalho, local para: Cadastro de clientes
# Ver clientes cadastrados, cadastro de produtos, ver produtos cadastrados, venda de produtos, relatório de vendas e a opção sair.
# Este menu deve se repetir até que a opção de sair for chamada.



menu = '''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                     I Festival de ituroró                                                 $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

1- Cadastro de produtos
2- Ver clientes
3- Cadastro de produtos
4- Ver produtos cadastredos
5- Vendas
6- Relatório de vendas
7- Sair

Digite a opção desejada: '''

opcao = input(menu)
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de clientes')
    elif opcao == '2':
        print('Ver clientes cadastrados')
    elif opcao == '3':
        print('Cadastro de produtos')
    elif opcao == '4':
        print('Ver produtos cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatório de vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor inválido')
