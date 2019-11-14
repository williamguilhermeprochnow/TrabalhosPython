dicionario_bandas = {'nome':''}
dicionario_bandas['Nome'] = 'Calipso'
dicionario_bandas['Nome'] = 'Dejavu'

print(dicionario_bandas)

dicionario = { 'Nome':'William', 'Sobrenome':'Guilherme'}
dicionario['Sobrenome'] = 'Prochnow'
dicionario['CPF'] = '123.456.789-10'

dicionario_pessoa = {'Nome':'', 'Sobrenome':'', 'CPF':'', 'RG':''}
lista_pessoas = []
for i in range(1,11):
    dicionario_pessoa['Nome'] = input('Digite o nome:')
    dicionario_pessoa['Sobrenome'] = input('Digite o sobrenome:')
    dicionario_pessoa['CPF'] = input('Digite o CPF:')
    dicionario_pessoa['RG'] = input('Digite o RG:')
print(dicionario_pessoa)
print(lista_pessoas)