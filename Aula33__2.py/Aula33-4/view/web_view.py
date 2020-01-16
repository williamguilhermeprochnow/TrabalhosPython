from flask import Flask, render_template
import sys
sys.path.append(r'C:\Github\Trabalhos Python\TrabalhosPython\Aula33__2.py\Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    enderecos = ec.listar_todo()
    return render_template('index.html', lista = pessoas, endereco = enderecos)

app.run(debug=True)