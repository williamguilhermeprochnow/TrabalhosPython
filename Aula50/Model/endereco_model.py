
class EnderecoModel:
    def __init__(self, logradouro, numero, complemento, id=None):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento