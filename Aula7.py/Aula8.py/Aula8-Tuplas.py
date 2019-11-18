# --- Aula 8 - 18-11-2019
# --- Tuplas

numeros = []
usuario = {'nome':'user', 'password':123456}
pessoa = ('William', 'Guilherme', 0, 45.5, numeros)

#print(numeros)
#print(usuario)
#print(pessoa)

numeros[1] = 5
usuario['password'] = 54321
lista_pessoas = []
lista_pessoas.append(pessoa)
pessoa[4][1] = 6
print(pessoa[4][1])
