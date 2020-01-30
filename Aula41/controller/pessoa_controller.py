from flask_restful import Resource

class PessoaController(Resource):

    def get (self):
        return 'Testando metodo HTTP GET'

    def post (self):
        return 'Testando metodo HTTP POST'

    def put (self):
        return 'Testando metodo HTTP PUT'

    def delete (self):
        return 'Testando metodo HTTP DELETE'
