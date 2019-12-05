# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"


##################################################### Bruno ######################################################################################
#>arquivo = open('Aula18.py\\arquivo.txt','r')
# conteudo = arquivo.read()

# #lista_da_primeira_linha = primeira_linha.split(',')

# linhas_do_arquivo = conteudo.split('\n')

# primeira_linha = linhas_do_arquivo[0]

# print('*'*50)
# print(primeira_linha)
# print('*'*50)
# print(primeira_linha.split(','))

# print(lista_da_primeira_linha[1])

#>registros = []
#>campos = ('codigo', 'nome', 'sexo', 'idade')


#>for linha in arquivo:
#>    dados = linha.strip().split(',')
#>    dicio = {}
#>    print(linha)
    # dicio['codigo'] = dados[0]
    # dicio['nome'] = dados[1] 
    # dicio['sexo'] = dados[2]
    # dicio['idade'] = dados[3]
#>    contador = 0
#>    for campo in dados:
#>        dicio[campo] = dados[contador]
#>        contador = contador + 1
    



        
#>    registros.append(dicio)
    #print(f'{dados[1]}: {dados[3]}')
    # for campo in dados:
    #     print(campo, len(campo))

#>print(registros)
############################################################## Abioluz ##########################################################################

def ler_cadastro():
   arquivo = open('Aula18.py\\arquivo.txt','r')
   lista = []
   for pessoas in arquivo:
      pessoas = pessoas.strip().split(',')
      dicionario = {'codigo':pessoas[0], 'nome':pessoas[1], 
                    'sexo':pessoas[2], 'idade':pessoas[3]}
      lista.append(dicionario)
   arquivo.close()
   return lista

def lista_festa(lista_de_entradas):
    lista_homens = []
    lista_mulheres = []

    for pessoa in lista_de_entradas:
        if int(pessoa['idade']) >= 18:
            if pessoa['sexo'] == 'f':
                lista_mulheres.append(pessoa)
            else:
                lista_homens.append(pessoa)
    
    salvar(lista_homens,'homens')
    salvar(lista_mulheres,'mulheres')

def salvar(lista,nome):
    arquivo = open(f'Aula18.py\\arquivo{nome}.txt','a')
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