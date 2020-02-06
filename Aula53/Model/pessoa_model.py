import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()
class PessoaModel(BaseAlchemy):
    __tablename__ = "pessoa"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length = 100))
    sobrenome = db.Column(db.String(length = 200))
    idade = db.Column(db.Integer)

    def __str__(self):
        return "{}|{} {} - {}".format(self.id, self.nome, self.sobrenome, self.idade)