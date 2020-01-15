#-------- Importar biblioteca do MySQLdb
import MySQLdb

class PessoaDb:
    #------- Configuração da conexão
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    #------ Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    #----- Criação do dicionário que representa uma pessoa
    #dicionario_pessoa = {'Id' : 0, 'Nome' : '', 'Sobrenome' : '', 'Idade' : 0, 'Endereco_Id' : 0}

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM pessoa"
        cursor.execute(comando_sql_select)
        #----- Pega todos os resultos da execução do comando SQL e armazena em uma variável
        resultado = cursor.fetchall()
        #primeira parte
        return resultado
    def buscr_por_id(self,id):
        comando_sql_select