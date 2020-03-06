# Crie uma classe passoa com:
#  3 atributos
#  7 Métodos


# Crie uma classe endereco com:
#  3 atributos
#  7 Métodos


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self. idade = idade
        self. cpf = cpf

    def set_nome(self, nome):
            self.nome = nome
    def get_nome(self):
            return self.nome

    def set_idade(self, idade):
        self.idade = idade
    def get_idade(self):
            return self.idade

    def set_cpf(self, cpf):
            self.cpf = cpf
    def get_cpf(self):
            return self.cpf


class Endereco:
    def __init__(self, rua, complemanto, referencia):
        self.rua = rua
        self.complemento = complemanto
        self.referencia = referencia

    def set_rua(self,rua):
        self.rua = rua
    def get_rua(self):
        return self.rua

    def set_complemento(self,complemento):
        self.complemento = complemento
    def get_complemento(self):
        return self.complemento

    def set_referencia(self,referencia):
        self.referencia = referencia
    def get_referencia(self):
        return self.referencia