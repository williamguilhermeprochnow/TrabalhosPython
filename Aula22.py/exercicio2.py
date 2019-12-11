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
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

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
    
    def salvar (self):
        arquivo = open('Aula22.py/arquivo.txt','a')
        arquivo.write(f'{self.codigo_cliente};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}')
        arquivo.close()
    
    def modificar_dados (self):
        self.cadastro = []
        arquivo = open('Aula22.py/cadastro2.txt','r')
        for linha in arquivo:
            linha_separada = inha.strip().split(';')
            dic = {
                'codigo':linha_separada[0],
                'nome':linha_separada[1],
                'idade':linha_separada[2],
                'sexo':linha_separada[3],
                'email':linha_separada[4],
                'telefone':linha_separada[5],
            }
            self.cadastro.append(dic)
        arquivo.close()



pess = Cliente(dadobruto)
pess.valor_bruto()
pess.salvar()
pess.modificar_dados()
print(f'codigo cliente: {pess.codigo_cliente+1}\nNome: {pess.nome}')
cad = Cliente()
print(cad.cadastro)