# Aula 21 - 12-12-2019


# Cliente.....

# Crie uma classe cliente.
# Use os seguintes atributos: codigo cliente(int), nome, idade(int), telefone, email, endereço
# Use o seguinte atributo de estado: crédito em R$, saldo R$, 
#                                    cliente_devedor(True/False)
# O atributo cliente_devedor deve ser True toda vez que o saldo negativo for menor 
# ou igual ao crédito. 
# Para o atributo cliente_devedor voltar a ser False o cliente deve pagar sua divida
# ficando com o saldo igual a 0 ou positivo.



# Como metodo use:
class Cliente:
    self.codigo_cliente = 0
    def __init__(self,codigo1, nome1, idade1, telefone1, email1, endereco1):
        self.codigo_cliente = codigo1
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.email = email1
        self.endereco = endereco1
        #
        self.credito = float
        self.saldo = float
        self.cliente_devedor = (True/False)

    def atualizar (self):
        '''
        Este metodo serve para atualizar o cadastro do cliente. 
        Os dados que podem ser atualizados são: 
        nome, idade(int), telefone, email, endereço
        '''
        self.nome = input(f'Digite seu nome: {nome1}')
        self.idade = int(input(f'Digite sua idade: {idade1}'))
        self.telefone = input(f'Digite seu telefone: {telefone1}')
        self.email = input(f'Digite seu email: {email1}')
        self.endereco = input(f'Digite o seu endereço: {endereco1}')

    def limite_credito(self,valor):
        '''
        O crédito é o valor máximo que o cliente pode ter de saldo negativo.
        Este metodo altera o valor tanto para aumentar o crédito quanto para 
        diminuir ou eliminar o crédito.
        Este valor deve ser passado como número negativo (ex: -50.00) para o atributo
        credito
        Se diminuir o crédito (exemplo de -50 para -10) e o 
        cliente ficar com o saldo menor que o cédito (exemplo saldo = -20 e cédito -10)
        o cliente_devedor fica True
        Se o cliente_devedor estiver True, o crédito pode ser diminuido porem não aumentado.
        
        '''
        if valor = limite_credito:
            limite_credito == -100.00
            'Você atingiu seu limite de crédido'
        elif limite_credito < -100.00:
            'Aumentou o crédito'
        else:
            'Diminuiu o crédito'
        
        

    def dinheiro(self,valor):
        '''
        Este metodo serve para adicionar/remover valor em R$ para o atributo saldo para 
        o cliente.
        Esta função recebe o valor como parametro. Se o valor for positivo, o saldo
        aumenta, se o valor for negativo o saldo diminui. 
        
        O cliente não pode ter seu saldo menor que o crédito. Então se o valor exceder
        deve retornar False e a operação fica cancelada.
        (Exemplo: limite do cartão de crédito)
        Caso o valor não exceda o crédito a operação será realizada, o valor do saldo
        irá diminuir e deve retornar True
        Se o cliente_devedor estiver True o dinheiro só poderá receber valores positivos.
        Se o cliente_devedor estiver True e o cliente depositar dinheiro suficiente para
        o saldo ficar maior ou igual a 0 o cliente_devedor deve ser alterado para False.
        '''
        if valor 

    def __eq__(self,valor):
        '''
        Este metodo deve comparar se o valor do código do cliente é igual ao valor.
        Se positivo ele retorna True caso contrário retorna False
        '''
        pass

    def __srt__(self):
        '''
        Este metodo deve retornar uma string com todos os dados do cliente.
        Use f-string para interpolar o texto com as variáveis
        '''
        pass



if __name__ == "__main__":

    '''
    Use este if para fazer os testes com a classe.
    Este if pergunta se este arquivo está sendo executado diretamente.
    Caso positivo o código será executado.
    '''
    pass
