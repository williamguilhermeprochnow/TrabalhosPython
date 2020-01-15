class Pessoa:
    id = 0
    nome = ''
    sobrenome = ''
    idade = 0
    endereco_id = 0

    def exportar_txt(lista_pessoas):
    #---- Cria uma arquivo e atribui uma variável 'arquivo'
    with open('TrabalhosPython/Aula33.py/exportacao_feita.txt','a') as arquivo:
        #Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoas:
            arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")
    #terceira parte
    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco_id}'