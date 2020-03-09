# Crie uma classe passoa com:
#  3 atributos
#  7 Métodos


# Crie uma classe endereco com:
#  3 atributos
#  7 Métodos

from Aula63.classe_endereco import Endereco


class Pessoa:
    def __init__(self, nome:str, sobrenome:str, idade:int, endereco:Endereco) -> int:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = 0
        self.__endereco = endereco

        if self.verfica_nome(nome):
            self.__nome = nome
        if self.verifica_sobrenome(sobrenome):
            self.__sobrenome = sobrenome

        if self.verifica_idade(idade):
            self.__idade = idade

    def verfica_nome(self, nome):
        if type(nome) == str:
            return True
        return False

    def verifica_idade(self, idade):
        if type(idade) == int and idade > 0:
            return True
        return False

    def verifica_sobrenome(self, sobrenome):
        if type(sobrenome) == str:
            return True
        return False


    def set_nome(self, nome) -> None:
        if self.verfica_nome(nome):
            self.__nome = nome
    def get_nome(self):
            return self.__nome

    def set_sobrenome(self, sobrenome) -> None:
        if self.verifica_sobrenome(sobrenome):
            self.__sobrenome = sobrenome
    def get_sobrenome(self):
        return self.__sobrenome

    def set_idade(self, idade) -> None:
        if self.verifica_idade(idade):
            self.__idade = idade
    def get_idade(self):
            return self.__idade

    # def get_endereco(self) -> Endereco:
    #     return self.__endereco
    #
    # def set_enereco(self, endereco: Endereco):






