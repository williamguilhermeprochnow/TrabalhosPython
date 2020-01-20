import MySQLdb
from Model.endereco import Endereco

class EnderecoDao:
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM endereço"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM endereço WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, endereco:Endereco):
        comando = f""" INSERT INTO endereço
        (
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            CIDADE,
            CEP
        )
        VALUES
        (
            '{endereco.logradouro}',
            '{endereco.numero}',
            '{endereco.complemento}',
            '{endereco.bairro}',
            '{endereco.cidade}',
            '{endereco.cep}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, endereco:Endereco):
        comando = f""" UPDATE endereço
        SET
            LOGRADOURO = '{endereco.logradouro}',
            NUMERO = '{endereco.numero}',
            COMPLEMENTO = '{endereco.complemento}',
            BAIRRO = '{endereco.bairro}',
            CIDADE = '{endereco.cidade}',
            CEP = '{endereco.cep}'
        WHERE ID = {endereco.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM endereço WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()