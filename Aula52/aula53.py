#ORM

from flask import Flask
from flask_restful import Api

from Aula52.Controller.produto_controller import ProdutoController


app = Flask(__name__)
api = Api(app)

#--- Rotas de PRODUTO
api.add_resource(ProdutoController, '/api/produto', endpoint='produtos')
api.add_resource(ProdutoController, '/api/produto/<int:id>', endpoint='produto')
app.run(debug=True)
