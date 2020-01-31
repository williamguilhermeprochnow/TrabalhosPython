import MySQLdb

from Aula41.Model.pessoa_model import PessoaModel
class PessoaDao:
    def __init__(self):
        self.connection = MySQldb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
        self.cursor = self.connection.cursor

    def list_all(self, id):
        self.cursor.execute("SELECT * FROM pessoa")
        pessoas = self.cursor.fetchall()
        lista_pessoa = []
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM pessoa WHER ID: ()".format(id))
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__

    def insert(self, pessoa):
        return 'Cadastrar a pessoa: {}' .format(pessoa)

    def update(self, pessoa):
        return 'Alterando a pessoa: {}' .format(pessoa)

    def remove(self, id):
        self.cursor.execute("DELETE FROM pessoa WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removendo a pessoa: {}' .format(id)