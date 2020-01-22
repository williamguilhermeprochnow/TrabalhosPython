import sys
sys.path.append('C:/Github/Trabalhos Python/TrabalhosPython/Aula35.py')
from Dao.squads_dao import SquadsDao
from Model.squads_model import Squads

class SquadsController:
    dao = SquadsDao()

    def salvar(self, squads:Squads):
        return self.dao.salvar(squads)

    def alterar(self, squads:Squads):
        self.dao.alterar(squads)

    def deletar(self, id):
        self.dao.deletar(id)