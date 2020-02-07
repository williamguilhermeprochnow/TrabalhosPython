import sqlalchemy as db

class BaseDao:
    def __init__(self):
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/aulabd")
        criador_sessao = db.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()