import sqlalchemy as db

from Aula55.model.base import Base

class Pessoa(Base):
    __tablename__ = 'LIVRARIA_PESSOA'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    data_nascimento = db.Column(db.DATE)
    naturalidade = db.Column(db.String(length=100))

    def __init__(self, nome, sobrenome, data_nascimento, naturalidade, id=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.naturalidade = naturalidade
        self.id = id

    def serialize(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "sobrenome" : self.sobrenome,
            "dataNasc" : str(self.data_nascimento),
            "naturalidade" : self.naturalidade
        }