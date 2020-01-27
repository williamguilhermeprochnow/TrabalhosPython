import MySQLdb

#host: mysql.padawans.dev

class FrontendDB():

    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans10', user='padawans10', passwd='wt2019')
    # ----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):

        comando_sql_select = "SELECT * FROM FrameworkFrontEnd;"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()

        return resultado

    def adicionar(self,nome):

        comando_sql_insert = f"INSERT INTO FrameworkFrontEnd (nome) values ('{nome}')"
        self.cursor.execute((comando_sql_insert))
        self.conexao.commit()
        id = self.cursor.lastrowid
        return id

    def buscar(self, id):

        comando_sql_select = f"SELECT * FROM FrameworkFrontEnd WHERE id= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def alterar(self, id, nome):
        comando_alterar = f"UPDATE FrameworkFrontEnd SET nome = '{nome}' where id = {id};"
        self.cursor.execute(comando_alterar)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM FrameworkFrontEnd WHERE id= {id}"
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()