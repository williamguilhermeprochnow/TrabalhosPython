# Testes em susuri

# Verificacao se determinada condição é verdadeira
# Checando se condições são veradeiras
assert  True
assert (10==10)
assert (10>5)
assert 'William' != 'Guilherme'

# Ciação de método para uso no teste
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

# Método com parâmetro opcional para o uso no teste
def multiplicacao (n1, n2, n3=1):
    return n1 * n2 * n3

# Método com condicional para uso no teste
def confirmando_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False

# Teste de resultado dos metodos acima
assert soma(5, 10) == 15
assert multiplicacao(2, 4, 6) == 48
assert confirmando_maioridade(18) == True
assert confirmando_maioridade(19) == True
assert confirmando_maioridade(17) == False
