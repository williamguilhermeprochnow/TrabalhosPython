import MySQLdb

from Aula50.Model import EnderecoModel

class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM endereço")
        enderecos = self.cursor.fetchall()
        lista_endereco = []
        for e in enderecos:
            endereco = EnderecoModel(e[1], e[2], e[3], e[0])
            lista_endereco.append(endereco.__dict__)
        return lista_endereco

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM endereço WHERE ID: ()".format(id))
        endereco = self.cursor.fetchone()
        e = EnderecoModel(endereco[1], endereco[2], endereco[3], endereco[0])
        return e.__dict__

    def insert(self, endereco:EnderecoModel):
        self.cursor.execute("INSERT INTO endereço (Logradouro , Número, Complemento) VALUES('{}','{}','{}')".format(endereco.logradouro, endereco.numero, endereco.complemento))
        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__init__

    def update(self, endereco : EnderecoModel):
        self.cursor.execute("UPDATE endereço SET Logradouro = '{}', Número = '{}', Complemento = '{}' WHERE ID = {}".format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.id))
        self.connection.commit()
        return endereco.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM endereço WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removendo o endereço: {}' .format(id)
