class Pessoa:
    def __init__(self, nome, idade, cpf, rua, complemento, numero, referecia):
        self.endereco = Endereco(rua, complemento, numero, referecia)
        self.nome = nome
        self.idade = 0
        self.cpf = cpf

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
    def set_endereco(self, endereco):
            self.endereco = endereco
    def get_endereco(self):
        return self.endereco


class Endereco:
    def __init__(self, rua, complemento, numero, referencia):
        self.rua = rua
        self.complemento = complemento
        self.numero = numero
        self.referencia = referencia

    def set_rua(self, rua):
        self.rua = rua
    def get_rua(self):
        return self.rua

    def set_complemento(self, complemento):
        self.complemento = complemento
    def get_complemento(self):
        return self.complemento

    def set_numero(self, numero):
        self.numero = numero
    def get_numero(self):
        return self.numero

    def set_referencia(self, referencia):
        self.referencia = referencia
    def get_referencia(self):
        return self.referencia

e = Endereco('piracanjuba', 'casa', 1200, 'do lado da casa')
print(e)
p = Pessoa('William', 17, 123456789, 'estrela', 'casa', 20, 'do lado da rua')
print(p)