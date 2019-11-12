# Crie um programa que lia 4 notas
# Imprima a maior nota
# Imprima a menor nota
# Imprima a média
# Imprima se o aluno foi aprovado ou reprovado (Média 7.0)

Nota1 = int(input('Digite nota 1:'))
Nota2 = int(input('Digite nota 2:'))
Nota3 = int(input('Digite nota 3:'))
Nota4 = int(input('Digite nota 4:'))

resultado = (f'{Nota1} +{ Nota2} + {Nota3} + {Nota4}')

Media = (Nota1 + Nota2 + Nota3 + Nota4)/4

if  Nota1 <= Nota2 and  Nota1 <= Nota3 and Nota1 <= Nota4:
    print(f'Menor nota é: {Nota1}')
elif Nota2 <= Nota1 and Nota2 <= Nota3 and Nota2 <= Nota4:
    print(f'Menor nota é: {Nota2}')
elif Nota3 <= Nota1 and Nota3 <= Nota2 and Nota3 <= Nota4:
    print(f'Menor nota é: {Nota3}')
#elif Nota4 <= Nota1 and Nota4 <= Nota2 and Nota4 <= Nota3:
else:
    print(f'Menor nota é: {Nota4}')

if  Nota1 >= Nota2 and  Nota1 >= Nota3 and Nota1 >= Nota4:
    print(f'Maior nota é: {Nota1}')
elif Nota2 >= Nota1 and Nota2 >= Nota3 and Nota2 >= Nota4:
    print(f'Maior nota é: {Nota2}')
elif Nota3 >= Nota1 and Nota3 >= Nota2 and Nota3 >= Nota4:
    print(f'Maior nota é: {Nota3}')
#elif Nota4 >= Nota1 and Nota4 >= Nota2 and Nota4 >= Nota3:
else:
    print(f'Maior nota é: {Nota4}')

print(f'A média do aluno é: {Media}')

if Media >= 7:
    print('Aprovado')
else:
    print('Reprovado')