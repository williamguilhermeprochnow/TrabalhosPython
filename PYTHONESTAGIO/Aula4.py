n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

print(f'soma: {n1} + {n2} = {n1 + n2}')
print(f'sub: {n1} - {n2} = {n1 - n2}')
print(f'mult: {n1} * {n2} = {n1 * n2}')
print(f'div: {n1} / {n2} = {n1 / n2}')

if n1 > n2:
    print(f'O numero {n1} é o maior')
elif n2 > n1:
    print (f'O numero {n2} é o maior')
else:
    print(f'Os numeros {n1} e {n2} são iguais')