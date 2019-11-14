#--- Exercício 3 - foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#            1- O nome dos alunos
#            2- Média do aluno
#            3- Resultado (Aprovado>=7.0)

lista = []

for i in range(0,10):

    lista.append(input('Digite o nome do aluno:'))
    n1 = float(input('Digite nota 1:'))
    n2 = float(input('Digite nota 2:'))
    n3 = float(input('Digite nota 3:'))
    n4 = float(input('Digite nota 4:'))
    média = float(f'{(n1 + n2 + n3 + n4) / 4}')
    print(média)
    if média >= 7.0:
        print('Aprovado')
    else:
        print('Reprovado')
    print(lista)