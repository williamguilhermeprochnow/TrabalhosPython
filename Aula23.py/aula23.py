total = 0,365
dias_de_cada_mes = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}

# qual_mes = int(input('Digite o número do mês:'))
# print('O mês', qual_mes, 'tem', dias_de_cada_mes[qual_mes], 'dias')
# print('Dias que faltam para acabar o ano, a partir do mês informado: ')
# print(sum(list(dias_de_cada_mes.values())[qual_mes-1:]))

# total = 0
# for mes in range(qual_mes, 12+1):
#     total += dias_de_cada_mes[mes]

# print('modo estruturado')
# print('total de dias até o final do ano', total)

for chave in dias_de_cada_mes:
    print('Tenho uma chave nessa linha', chave)
    print('se eu tenho uma chave, tenho o valor', dias_de_cada_mes[chave])

for chave, valor in dias_de_cada_mes.items():
    print('para a chave', chave, 'o valor', valor)

# tupla = ('Texto', 42, 5.01, int, str, list)

tupla = ('Text', 'texto de novo', 'textei', 'textamento')
for isto in tupla:
    print(type(isto))
    print(isto)
