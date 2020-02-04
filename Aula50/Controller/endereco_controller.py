from flask_restful import Resource
from flask import request

from Aula50.Dao.endereco_dao import EnderecoDao
from Aula50.Model.endereco_model import EnderecoModel

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get (self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post (self):

        logradouro = request.json['logradouro']
        numero = request.json['numero'] #pode ser com letras
        complemento = request.json['complemento']
        endereco = EnderecoModel(logradouro, numero, complemento)

        msg = self.dao.insert(endereco)
        return msg

    def put (self, id):
        logradouro = request.json['logradouro']
        numero = request.json['numero'] #pode ser com letras
        complemento = request.json['complemento']
        endereco = EnderecoModel(logradouro, numero, complemento, id)
        msg = self.dao.update(endereco)
        return msg

    def delete (self, id):
        return self.dao.remove(id)
