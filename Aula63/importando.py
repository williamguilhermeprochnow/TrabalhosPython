from Aula63.classe_pessoa import Pessoa
from Aula63.classe_endereco import Endereco

class Funcionario(Pessoa):
    def __init__(self, registro, cargo, nome, sobrenome, idade, endereco):
        super().__init__(nome, sobrenome, idade, endereco)
        self.__numero_registro = registro
        self.__cargo = cargo

    def set_registro(self, numero_registro) -> None:
        self.__numero_registro = numero_registro

    def set_cargo(self, cargo) -> None:
        self.__cargo = cargo


    def get_registro(self) -> int:
        return self.__numero_registro

    def get_cargo(self) -> int:
        return self.__cargo


# f = Funcionario('', '', '', '', '', '')
# f.set_nome('William')
# f.set_sobrenome('Prochnow')
# f.set_cargo('Programador')
# f.set_idade(17)
# f.set_registro(123456)
#
# print(f.get_nome())
# print(f.get_sobrenome())
# print(f.get_cargo())
# print(f.get_idade())
# print(f.get_registro())


end = Endereco('', '', '')
end.set_rua('Gonçalvez')
end.set_complemento('Casa')
end.set_numero('200')

print(end.get_rua())
print(end.get_complemento())
print(end.get_numero())