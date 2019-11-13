#2 -
# Mercado Tch ----
# Solicitar nome do funcionario
# solicitar idade
# Informar se o funcionario pode adquirir produtos alcoolicos
 
#3 -
# Cadastro prudutos Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolico e não alcoolicos)
#  Exibir o produto cadastrdo


#2 - 

print('Mercado Tech')
Funcionario = (input('Nome do Funcionário:'))
Idade = int(input('Idade:'))
if Idade >= 18:
    print('É permitido adquirir bebidas alcoolicas')
else:
    print('Não é permitido adquirir bebidas alcoolicas')

#3 - 

print('Produto do Mercado Tech')
Nomep = input('Digite o nome do produto:')
categoria = int(input('informe a categoria do produto 1-Alcoolico e 2-Não alcoolico:'))

if categoria ==1:
    print(f'O nome do produto é {Nomep} e ele é alcoolico')
elif categoria ==2:
    print(f'O nome do produto é {Nomep} e ele não é alcoolico')
else:
    print('Categoria não existe')