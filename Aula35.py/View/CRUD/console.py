import sys
sys.path.append('/Github/Trabalhos Python/TrabalhosPython/Aula35.py')
from Controller.squads_controller import SquadsController
from Model.squads_model import Squads

squads = Squads()
squads.nome = 'WD'
squads.descricao = 'Hakis'
squads.numero_de_membros = 4
squads.linguagem_back_end = 'Python'
squads.framework_front_end = 'HTML'

controller = SquadsController()
controller.salvar(squads)

################################################ Tabela squads ##################################################################################

#salvar(conexao, cursor, 'Rush', 'Vem tranquilo', 4, 'Python', 'Angular')
#alterar(conexao, cursor, 2, 'WZ', 'Afoba não', 5, 'JSP', 'HTML')
#deletar(conexao, cursor, 3)