# Aula 6 - 13/11/2019
# Listas

#--- Inicialização de uma variavel do tipo lista
lista1 = []
#--- Inicialização de uma variável lista, com elementos
lista2 = ['Marcela', 'Nicole' , '*Matheus',10]
#--- Lista de inteiros
lista3 = [1,2,3,5]

#--- Impressão de lista criadas
print(lista1)
print(lista2)
print(lista3)

#---- Adicionados elementos ja criados
lista1.append(lista2)
lista1.append(lista3)
lista1.append(input('Digite seu artista favorito:'))
#---Criação da lista com dados vindos da funçao input
lista_perguntas = [input('Digite seu artista favorito:'), input('Digite seu guitarrista favorito:')]

print(list_pergunta)



posicao = int(input('Digite a posição:'))
print(lista2[posicao -1])
print(lista1)