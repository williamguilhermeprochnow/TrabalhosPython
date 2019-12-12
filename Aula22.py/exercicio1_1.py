# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class Cliente ():
    def __init__ (self, dadobruto):
        self.dado_bruto = dadobruto
        self.codigo_cliente = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
    
    def valor_bruto (self):
        Cliente = self.dado_bruto.strip().split(';')
        self.codigo_cliente = int( Cliente[0] )
        self.nome = Cliente[1]
        self.idade = int( Cliente[2] )
        self.sexo = Cliente[3]
        self.email = Cliente[4]
        self.telefone = Cliente[5]

pess = Cliente(dadobruto)
pess.valor_bruto()

print(f'codigo cliente: {pess.codigo_cliente+1}\nNome: {pess.nome}\nIdade: {pess.idade}\nSexo: {pess.sexo}\nEmail: {pess.email}\nTelefone: {pess.telefone}')