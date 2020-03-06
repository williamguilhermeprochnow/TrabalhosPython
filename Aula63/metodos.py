def soma(n1, n2):
    n1 = n1
    n2 = n2
    resultado = int(n1 + n2)
    return resultado

def mult(n1,n2,n3=1):
    n1 = n1
    n2 = n2
    n3 = n3
    return n1*n2*n3

def somastr():
    str1 = ('Digite a strig1:')
    str2 = ('Digite a strig2:')
    reultado = str(str1 + str2)
    return reultado

print(soma((int(input('Digite n1: ')), int(input('Digite n2: ')))))


print(mult(2,2))

print(somastr(input('Digite str1: '), input('Digite str2: ')))