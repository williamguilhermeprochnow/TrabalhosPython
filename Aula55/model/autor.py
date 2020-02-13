import sqlalchemy as db
from sqlalchemy.orm import relationship

from Aula55.model.pessoa import Pessoa
from Aula55.model.base import Base
from Aula55.dao.pessoa_dao import PessoaDao

class Autor(Base):
    __tablename__ = "LIVRARIA_AUTOR"
    id = db.Column(db.Integer, primary_key=True)
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.id'))
    pessoa = relationship(Pessoa)

    def __init__(self, pseudonimo, descricao, pessoa_id, pessoa, id=None):
        self.pseudonimo = pseudonimo
        self.descricao = descricao
        self.pessoa_id = pessoa_id
        self.pessoa = pessoa
        self.id = id

    def serialize(self):
        return {
            "id" : self.id,
            "pseudonimo" : self.pseudonimo,
            "descricao" : self.descricao,
            "pessoa_id" : self.pessoa_id,
            "pessoa" : self.pessoa.serialize()
        }