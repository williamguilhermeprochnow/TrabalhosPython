# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'], 
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


# 2 - usando o for, imprima todos nomes um abaixo do outro
#
# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)



for i in cadastroHBSIS:
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][1]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][1]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][1]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][1]}')
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][2]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][2]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][2]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][2]}')
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][3]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][3]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][3]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][3]}')
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][3]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][4]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][4]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][4]}')
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][5]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][5]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][5]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][5]}')
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][6]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][6]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][6]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][6]}')
    print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][7]}\n{cadastroHBSIS[2]}: {cadastroHBSIS[3][7]}\n{cadastroHBSIS[6]}: {cadastroHBSIS[7][7]}\n{cadastroHBSIS[4]}: {cadastroHBSIS[5][7]}')
    break
    