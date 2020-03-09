class Endereco:
    def __init__(self, rua:str, complemento:str, numero:str) -> int:
        self.__rua = rua
        self.__complemento = complemento
        self.__numero = numero

        if self.verfica_rua(rua):
            self.__rua = rua
        if self.verifica_complemento(complemento):
            self.__complemento = complemento

        if self.verifica_numero(numero):
            self.__numero = numero

    def verfica_rua(self, rua):
        if type(rua) == str:
            return True
        return False

    def verifica_complemento(self, complemento):
        if type(complemento) == str:
            return True
        return False

    def verifica_numero(self, numero):
        if type(numero) == int or type(numero) == float or type(numero) == str and numero > 0:
            return True
        return False


    def set_rua(self, rua) -> None:
        if self.verfica_rua(rua):
            self.__rua = rua
    def get_rua(self):
            return self.__rua

    def set_complemento(self, complemento) -> None:
        if self.verifica_complemento(complemento):
            self.__complemento = complemento
    def get_complemento(self):
        return self.__complemento

    def set_numero(self, numero) -> None:
        if self.verifica_numero(numero):
            self.__numero = numero
    def get_numero(self):
            return self.__numero

en = Endereco('t', 'casa', 3)
print(en)

