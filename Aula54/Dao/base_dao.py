import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker

class BaseDao:
    def __init__(self, model_type):
        self.model_type = model_type
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/aulabd")
        criador_sessao = db.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()

    def listar_todos(self) -> list:
        return self.sessao.query(self.model_type).all()

    def buscar_por_id(self, id):
        return self.sessao.query(self.model_type).filter_by(id=id).one()

    def deletar(self, id) -> str:
        model = self.sessao.query(self.model_type).filter_by(id=id).one()
        self.sessao.delete(model)
        self.sessao.commit()
        return 'Deletado objeto de id: {}'.format(id)

    def inserir(self, model) -> str:
        self.sessao.add(model)
        self.sessao.commit()
        return 'Objeto de id {} foi criado'.format(model.id)

    def alterar(self, model) -> str:
        self.sessao.merge(model)
        self.sessao.commit()
        return 'Objeto {} foi alterado com sucesso'.format(model.nome)