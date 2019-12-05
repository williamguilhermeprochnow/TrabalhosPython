# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing

def ler_cadastro():
    arquivo = open('Aula19.py\\cadastro.txt','r')
    lista = []
    for pessoas in arquivo:
        pessoas = pessoas.strip().split(';')
        dicionario = {'codigo':pessoas[0], 'nome':pessoas[1],'idade':pessoas[2], 'sexo':pessoas[3], 'e-mail':pessoas[4], 'telefone':pessoas[5]}
        lista.append(dicionario)
    arquivo.close()
    return lista

def lista_festa(lista_de_entradas):
    lista_homens = []
    lista_mulheres = []

    for pessoa in lista_de_entradas:
        if int(pessoa['idade']) >= 18:
            print(f'Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!"')
            if pessoa['sexo'] == 'f':
                lista_mulheres.append(pessoa)
            else:
                lista_homens.append(pessoa)
    
    salvar(lista_homens,'homens')
    salvar(lista_mulheres,'mulheres')

def salvar(lista,nome):
    arquivo = open(f'Aula19.py\\arquivo{nome}.txt','a')
    for pessoa in lista:
        texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}\n"
        arquivo.write(texto)
    arquivo.close()

def consulta(lista_consulta_funcao,numero):
    for lista_consulta in lista_consulta_funcao:
        if int(lista_consulta['idade']) >= 18:
            if lista_consulta['sexo'] == 'f':
                print(f"Nome: {lista_consulta['nome']} Valor do ingresso: R$ 15,00")
            else:
                print(f"Nome: {lista_consulta['nome']} Valor do ingresso: R$ 35,00")
        else:
            print('Não pode entrar!')

lista1 = ler_cadastro()
lista_festa(lista1)

while True:
    a = int(input('Digite um número: '))
    consulta(lista1,a)

for i in lista_festa:
    print(i)

lista1 = ler_cadastro()
print(lista1)

#####