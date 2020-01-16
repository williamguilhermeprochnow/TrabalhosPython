import sys
sys.path.append('/Github/Aulas Python/AulasPython/33-Aula33/Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

pc = PessoaController()
ec = EnderecoController()

for p in pc.listar_todos():
    print(p)

for e in pc.listar_todos():
    print(e)