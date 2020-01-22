class Squads:
    id = 0
    nome = ''
    descricao = ''
    numero_de_membros = 0
    linguagem_back_end = ''
    framework_front_end = ''


    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numero_de_membros};{self.linguagem_back_end};{self.framework_front_end}'