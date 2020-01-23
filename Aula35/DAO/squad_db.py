import MySQLdb

#host: mysql.padawans.dev

class SquadDB():

    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root')
    # ----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):

        comando_sql_select = "SELECT * FROM squads"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()

        return resultado

    def adicionar(self,nome, descricao, numero_pessoas, linguaguem_back_end, framework_front_end):

        comando_sql_insert = f"INSERT INTO squads (nome, descricao, Numero_de_membros, linguagem_back_end, framework_front_end) VALUES ('{nome}', '{descricao}', {numero_pessoas}, '{linguaguem_back_end}', '{framework_front_end}')"
        self.cursor.execute((comando_sql_insert))
        self.conexao.commit()

    def buscar(self, id):

        comando_sql_select = f"SELECT * FROM squads WHERE id= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def alterar(self, id, nome, descricao, numero_pessoas, linguaguem_back_end, framework_front_end):
        comando_alterar = f"update squads SET nome = '{nome}', descricao = '{descricao}', Numero_de_membros = {numero_pessoas}, linguagem_back_end = '{linguaguem_back_end}', framework_front_end = '{framework_front_end}' where id = {id};"
        self.cursor.execute(comando_alterar)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM squads WHERE id= {id}"
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()