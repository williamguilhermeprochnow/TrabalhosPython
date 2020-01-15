#======== Estrutura de dados e DB

#-------- Importar biblioteca do MySQLdb
import MySQLdb

def listar_todos():
    #------- Configuração da conexão
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    #------ Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    #----- Criação do dicionário que representa uma pessoa
    #dicionario_pessoa = {'Id' : 0, 'Nome' : '', 'Sobrenome' : '', 'Idade' : 0, 'Endereco_Id' : 0}


    #----- Criação do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM pessoa"
    cursor.execute(comando_sql_select)
    #----- Pega todos os resultos da execução do comando SQL e armazena em uma variável
    resultado = cursor.fetchall()
    #primeira parte
    return resultado

def converter_tabela_dicionario(lista_tuplas):
#Cria uma lista para armazenar os dicionários
    lista_pessoas = []
    for p in lista_tuplas:
        #---- Criação do dicionário q representa uma pessoa
        dicionario_pessoa = {'Id' : 0, 'Nome' : '', 'Sobrenome' : '', 'Idade' : 0, 'Endereco_Id' : 0}
        #---- Pega cada posição a tupla e atribui a uma chave do dicionário
        dicionario_pessoa['Id'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_Id'] = p[4]
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas
#segunda parte

def exportar_txt(lista_pessoas)
#---- Cria uma arquivo e atribui uma variável 'arquivo'
with open('TrabalhosPython/Aula33.py/pessoas.txt','a') as arquivo:
    #Percorre a lista de dicionário e salva no arquivo em formato pré-definido
    for p in lista_pessoas:
        arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")
#terceira parte

lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)