# Aula 15 - 28/11/2019
# Manipulação de arquivos

def salvar_pessoa(pessoa_dicionario):
    arquivo = open('aula15.txt','w')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt','r')
    for linha in arquivo:
        lista.append(linha)
    arquivo.close()
    return lista

nome = input('Digite nome: ')
sobrenome = input('Digite sobrenome: ')
idade = int(input('Digite a idade: '))


pessoa = {'nome':nome, 'sobrenome':sobrenome, 'idade':idade}
salvar_pessoa(pessoa)

print( ler() )


# arquivo = open('aula15.txt','r')
# for linha in arquivo:
#     print(linha)
# arquivo.close()