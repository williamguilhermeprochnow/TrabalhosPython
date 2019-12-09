# Aula 22 - 09/10/2019

# 1) O que uma pessoa tem? Quais as características?
###### Atributos --- Variáveis
# nome
# idade
# telefone
# sexo

# 2) O que uma pesso a faz?
# ###### metodos (Função/procedimento)
# respira
# dorme
# corre
# bebe
# multiplica  ####

# 3) Como a pessoa está agora?
# ###### Atributos de estado - Variáveis
# divida
# cansada
# viva
# fome
# sede


class Pessoa:
    '''
    Esta classe é uma demonstração para aula
    '''
    def __init__ (self,nome1, idade1, telefone1, sexo1):
        '''
        O __int__ é o motor que irá iniciar as variávei da classe.
        O self é o que irá conectar toda classe
        '''
        # Atributos ################
        self.nome = nome1
        self.idade1 = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        #
        self.divida = None
        self.cansada = 'Não'
        self.viva = True
        self.fome = 'Não'
        self.sede = 'Não'

    ##### Métodos

    def respira (self,respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False

    def corre (self,distancia):
        if self.viva:
            if distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >=100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'
    
    def dorme (self):
        if self.viva:
            self.cansada = 'Não'
            self.bebe()
            self.come()

    def bebe (self):
        if self.viva:
            self.sede = 'Não'


    def come (self):
        if self.viva:
            self.fome = 'Não'

    def multiplica (self):
        pass




p = Pessoa('Antônio', 18, '4791234567', 'm')

# p.respira(False)

# p.respira(True)

p.corre(600)
p.dorme()
# p.come()
# p.bebe()

print(f'Nome é: {p.nome}')
print(f'Está vivo?: {p.viva}')
print(f'Está com fome?: {p.fome}')
print(f'Está com sede?: {p.sede}')
print(f'Está cansado?: {p.cansada}')

#(atributos, metodos, atributos estado)