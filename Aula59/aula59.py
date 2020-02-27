#--- Metodos
#--- Argumentos Ordenados
#--- Argumentos Nomeados
#--- Argumento Opcionais

# Métodos para uso de parametros ordenados
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

res = soma(10,20)
print(res)

# Métodos para uso de parametros nomeados
def subtracao (n1, n2,n3):
    resultado = n1 - n2 - n3
    return resultado

res2 = subtracao(n3=10, n2=20, n1=30)
print(res2)

# Métodos para uso de parametros opcionais
def multiplicacao (n1, n2, n3=1):
    return n1 * n2 * n3

res3 = multiplicacao(10,20)
print(res3)

