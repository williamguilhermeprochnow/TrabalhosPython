# 3 - Criar um programa para o cadastro do cliente
# Para o cadastro de clientes deve pedir os seguintes dados: Código do cliente, CPF, Nome completo, Data de nascimento, Estado, Cidade, cep,
# bairro, rua, número da casa, complemento.

def cadastro_cliente():
    dados_cliente = ['Código_cliente', 'CPF', 'Nome_completo', 'Data de nascimento', 'Estado', 'Cidade', 'cep', 'Bairro', 'Rua', 'Número da casa', 'Complemento']

    lista = []

    for j  in range(numero_funcao):
        dicionario = {}

        for i in dados_cliente:
            dicionario[i]= input(f'{i}: ')
        lista.append(dicionario)
    return lista

numero = int(input('Digite o número de cadastros: '))

lista_cadastro = cadastro_cliente(numero)

#lista_cadastro = [{'Código_cliente', 'CPF', 'Nome_completo', 'Data de nascimento', 'Estado', 'Cidade', 'cep', 'Bairro', 'Rua', 'Número da casa', 'Complemento'}]
# Criar uma função para salvar em arquivo:


for cliente in lista_cadastro:
    cliente_chave = list(cliente.keys())
    for chaves in cliente_chave:
        salva = f'{cliente[chaves]}'


arquivo.write()


arquivo.close()

# Continua...