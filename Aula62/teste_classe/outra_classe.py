from Aula62.teste_classe.classe import Pessoa

class Engenheiro(Pessoa):
    def __init__(self, mecanico, civil, nome, cpf, rua, complemento, numero, referecia):
        super().__init__(nome, cpf, rua, complemento, numero, referecia)
        self.mecanico = mecanico
        self.civil = civil

    def set_mecanico(self, mecanico):
            self.mecanico = mecanico
    def get_mecanico(self):
        return self.mecanico

    def set_civil(self, civil):
            self.civil = civil
    def get_civil(self):
        return self.civil

E = Engenheiro()