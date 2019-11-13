#--- Exercício 1 - listas
#--- Escreva programa que leia o nome 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima a lista

lalunos = []

for i in range(1,11):
    nomes = input('Digite seu nome:')
    lalunos.append(nomes)
print(lalunos)
