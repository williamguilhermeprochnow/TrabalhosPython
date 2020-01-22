import sys
sys.path.append('C:/Github/Trabalhos Python/TrabalhosPython/Aula35.py')
import MySQLdb
from Model.squads_model import Squads

################################################ Tabela squads ##################################################################################

class SquadsDao:
    conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root')
    cursor = conexao.cursor()

    #Salvar nome do squad
    def salvar(self, squads:Squads):
        comando = (F"INSERT INTO squads (Nome, Descricao, Numero_de_membros, Linguagem_Back_End, Framework_Front_End)VALUES('{squads.nome}', '{squads.descricao}', {squads.numero_de_membros}, '{squads.linguagem_back_end}', '{squads.framework_front_end}')")
        self.cursor.execute(comando)
        self.conexao.commit()

    #Alterar squad
    def alterar(self, squads:Squads):
        comando = (f"UPDATE squads SET Nome='{squads.nome}', Descricao='{squads.descricao}', Numero_de_membros={squads.numero_de_membros}, Linguagem_Back_End='{squads.linguagem_back_end}', Framework_Front_End='{squads.framework_front_end}' WHERE ID={squads.id}")
        self.cursor.execute(comando)
        self.conexao.commit()


    #Deletar squad
    def deletar(self, id):
        comando = (f'DELETE FROM squads WHERE ID={id}')
        self.cursor.execute(comando)
        self.conexao.commit()