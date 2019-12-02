# Aula 17 - 02/11/2019
# Dicinários, while

# bole = True
n=0

# while bole:
#     n = n + 1
#     print(f'Ola turma {n}')

# while n <= 30:
#     n= n + 1
#     print(f'Ola turma {n}')

# while False:
#     n = n + 1
#     print(f'Ola turma {n}')

while n <=30:
    n = n + 1
    print(f'Ola turma {n}')
    break
    print('Passou!')

while n <=30:
    n = n + 1
    print(f'Ola turma {n}')
    if n == 10:
        continue
    print('Passou!')