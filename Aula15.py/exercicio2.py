# --- Mesma coisa, agora com o assunto cerveja.
# --- Cerveja, Marca, Tipo e Teor.



def cerveja_1(cerveja_dicionario):
    arquivo = open('exercicio2.txt','a')
    arquivo.write(f"{cerveja_dicionario['Cerveja']};{cerveja_dicionario['Marca']};{cerveja_dicionario['Tipo']};{cerveja_dicionario['Teor']}\n")
    arquivo.close()

def ler():
    ambev = []
    arquivo = open('exercicio.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        ambev_linha = linha.split(';')
        cerveja = {'Cerveja':ambev_linha[0], 'Marca':ambev_linha[1], 'Tipo':ambev_linha[2], 'Teor':ambev_linha[3]}
        ambev.append(cerveja)
    arquivo.close()
    return ambev

cerveja = ler()
for p in cerveja:
    print(f"{p['Cerveja']} - {p['Marca']} - {p['Tipo']} - {p['Teor']}")

cerveja = 'Cerveja'
print(cerveja)
Marca = input('Digite a marca:')
Tipo = input('Digite o tipo:')
Teor = 'Teor: 7,5%'

print(Teor)

cerveja = {'Cerveja':cerveja, 'Marca':Marca, 'Tipo':Tipo, 'Teor':Teor}
cerveja_1(cerveja_2)


