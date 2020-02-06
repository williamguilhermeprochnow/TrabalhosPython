from Aula53.dao.base_dao import BaseDao
from Aula53.Model.pessoa_model import PessoaModel

class PessoaDao(BaseDao):
    def list_all(self):
        return self.sessao.query(PessoaModel).all()