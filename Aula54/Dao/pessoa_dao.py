from Aula54.Dao.base_dao import BaseDao
from Aula54.Model.pessoa_model import PessoaModel

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(PessoaModel)