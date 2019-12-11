# Aula 21 - 09/12/2019

# Crie uma classe cliente

# Deve ter como atributos: codigo, cpf, nome, idade, sexo

# Como metodos: receber salario, comprar

# Quando recebe aumenta o dinheiro na carteira.

# Quando compra aumenta os bens e diminui o dinheiro na carteira;

# Se comprar e não tivar dinheiro suficiente deve diminuir o dinheiro da carteira e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) Atributos de estado: dinheiro na carteira, divida, bens

class cliente:
    def __init__ (self,codigo1, cpf1, nome1, idade1, sexo1, compra1):
        self.codigo = codigo1
        self.cpf = cpf1
        self.nome = nome1
        self.idade = idade1
        self.sexo = sexo1
        #
        self.salario = 2500
        self.bens = 0
        self.compra = None
        self.divida = 0
        self.dinheiro_carteira = 0

    def receber (self, salario = None):
        if salario == None:
            salario = self.salario
        if self.dinheiro_carteira == 0:
            self.dinheiro_carteira = salario
        else:
            self.dinheiro_carteira += salario

    def comprar (self, compra = None):
        if compra == None:
            compra = self.compra
        if self.dinheiro_carteira > compra:
            self.divida = 'Inexistente'
        else:
            self.divida = 'Existente'


    # def set_divida (self, divida = None):
    #     if divida == None:
    #         divida = self.divida
    #     if self.divida == 0:
    #         self.divida = dinheiro_carteira < self.compra
    #     else:
    #         self.divida == 0

# cliente = Empregado(1,22222222, 'Wiliam', 17, 'm', 2500 )
# cliente1 = Empregado(2,33333333, 'paulo', 18, 'm', 4000)

# print(cliente.nome)
# print(cliente.salario)
# print(cliente.compra)

# print(cliente1.nome)
# print(cliente1.salario)
# print(cliente1.compra)