from flask import request

from Aula52.Controller.base_controller import BaseController
from Aula52.Dao.produto_dao import ProdutoDao
from Aula52.Model.produto_model import ProdutoModel

class ProdutoController(BaseController):
    def __init__(self):
        super().__init__(ProdutoDao())


    def post(self):
        self.carrega_parametros()
        model = ProdutoModel(self.nome, self.descricao)
        return super().post(model)

    def put(self, id):
        self.carrega_parametros()
        model = ProdutoModel(self.nome, self.descricao, id)
        return super().put(model)

    def carrega_parametros(self):
        self.nome = request.json['nome']
        self.descricao = request.json['descricao']