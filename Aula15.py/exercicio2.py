# --- Mesma coisa, agora com o assunto cerveja.
# --- Cerveja, Marca, Tipo e Teor.

################################################### area do metodo ######################################################

def cerveja_1(cerveja_dicionario):
    arquivo = open('exercicio2.txt','a')
    arquivo.write(f"{cerveja_dicionario['Cerveja']};{cerveja_dicionario['Marca']};{cerveja_dicionario['Tipo']};{cerveja_dicionario['Teor']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('exercicio2.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        ambev_linha = linha.split(';')
        cerveja = {'Cerveja':ambev_linha[0], 'Marca':ambev_linha[1], 'Tipo':ambev_linha[2], 'Teor':ambev_linha[3]}
        lista.append(cerveja)
    arquivo.close()
    return lista

############################################################ area do codigo #####################################################################
cerveja = input('Digite a quantidade: ')
Marca = input('Digite a marca: ')
Tipo = input('Digite o tipo: ')
Teor = input('Digite o teor: ')


dic = {'Cerveja':cerveja, 'Marca':Marca, 'Tipo':Tipo, 'Teor':Teor}
cerveja_1(dic)


for p in ler():
    print(f"{p['Cerveja']} - {p['Marca']} - {p['Tipo']} - {p['Teor']}")

# cerveja = 'Cerveja'
# print(cerveja)


# print(Teor)



