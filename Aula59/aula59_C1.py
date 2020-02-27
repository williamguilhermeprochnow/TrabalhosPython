# Rev Classe
# Métodos de classe
# Método __init__ = construtor
# Variáveis de classe
# Variávei privadas
# Variáveis
# Metodos Getters e Setters

class Calc:

    def __init__(self, numero1, numero2):
        # Variavel da classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        __resultado = self.__n1 + self.__n2
        return self.__resultado

    def subtracao(self):
        __resultado = self.__n1 - self.__n2

    def multiplicacao(self):
        __resultado = self.__n1 * self.__n2

# Instanciando um objetoda classe calc
c = Calc(10,20)
print(c.get_n1())
print(c.get_n2())
c.set_n1(1000)
c.set_n2(1800)
print(c.get_n1())
print(c.get_n2())
print(c.get_resultado())