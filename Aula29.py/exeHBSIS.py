#--- Dias 06 e 07/01/2020

# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

#Só o piloto, Chefe e o Policial podem dirigir o veículo (Fortwo)
#Nenhum dos oficiais pode ficar sozinho com o chefe
#Nenhuma das comissárias pode ficar sozinhas com o piloto
#O presidiário não podera ficar sozinho com os tripulantes sem a presença de um policial, no terminal e no avião

el1='Piloto'
el2='Oficial 1'
el3='Oficial 2'
el4='chefe de serviço de voo'
el5='comissária 1'
el6='comissária 2'
el7='Bandido'
el8='Policial'
carro = []
aviao = []
terminal = [el1,el2,el3,el4,el5,el6,el7,el8]
numero_viagem=0

def ler_lista():
    arquivo = open('TrabalhosPython/Aula29.py/listas.txt','r')
    lista = []
    for ler in arquivo:
        linha = ler.strip()
        lista.append(linha)  
    arquivo.close()
    return lista
print(ler_lista())

def viagem_fortwo():
    global numero_viagem
    numero_viagem += 1
    print(f'\n========== Viagem {numero_viagem} ==========')
    print(f'Estão no terminal: {", ".join(terminal)}')
def embarque(mot, pas):
    terminal.remove(mot)
    terminal.remove(pas)    
    carro.append(mot)
    carro.append(pas)
    print(f'A {mot} e o {pas} embarcaram no Fortwo e vão até o avião')
    print(f'A {pas} desce do Fortwo e embarca no avião ')
    carro.remove(pas)
    aviao.append(pas)
    print(f'O {mot} volta no Fortwo para o terminal')
    terminal.append(mot)   
def embarques(mot,pas):
    terminal.remove(mot)
    terminal.remove(pas)
    carro.append(mot)
    carro.append(pas)
    print(f'O {mot} e o {pas} entram no fortwo e vão até o avião')
    carro.remove(mot)
    carro.remove(pas)
    aviao.append(mot)
    aviao.append(pas)
    print(f'O {mot} e o {pas} saem do fortwo e entram no avião')
for viagem in range(1,8):
    if viagem == 1:
        viagem_fortwo()
        embarque(el4, el5)
        print(f'Estão no avião: {", ".join(aviao)}')
    elif viagem == 2:
        viagem_fortwo()
        embarque(el4,el6)
        print(f'Estão no avião: {", ".join(aviao)}')
    elif viagem == 3:
        viagem_fortwo()
        embarque(el1,el2)
        print(f'Estão no avião: {", ".join(aviao)}')
    elif viagem == 4:
        viagem_fortwo()
        embarque(el1,el3)
        print(f'Estão no avião: {", ".join(aviao)}')
    elif viagem == 5:
        viagem_fortwo()
        embarque(el1,el4)
        print(f'Estão no avião: {", ".join(aviao)}')
    elif viagem == 6:
        viagem_fortwo()
        embarque(el8,el1)
        print(f'Estão no avião: {", ".join(aviao)}')
    elif viagem == 7:
        viagem_fortwo()
        embarques(el7,el8)
        print(f'Estão no avião: {", ".join(aviao)}\n')

print(f'Já foram de avião os passageiros: {", ".join(aviao)}')

#######################################     PRIMEIRA VERSÃO FEITA E ESTRAGADA PELO EXERCÍCIO SEGUINTE       ######################################

# passageiros = []
# aguardando = []

# def LevandoP (motorista1, motorista2):
#     print(f'Fortwo está com {motorista1} e {motorista2}')
#     print(f'Desembarca {motorista2}')
#     aguardando.append(motorista2)
#     print(f'Volta {motorista1}')

# def embarques (motorista, passageiro):
#     passageiros.append(passageiro)
#     print(f'Fortwo está indo ao terminal com o {motorista} e {passageiro}')
#     print(f'Chegou ao terminal e desembarcou somente o {passageiro}')
#     print(f"As pessoas que ja estão no terminal {', '.join(passageiros)}")
#     print(f'Fortwo esta voltando com {motorista} \n')

# def passageiromotorista(motorista, passageiro):
#     passageiros.append(passageiro)
#     passageiros.append(motorista)
#     print(f'Fortwo está indo ao terminal com o {motorista} e o {passageiro}')
#     print(f'Fortwo chegou ao terminal')
#     print(f"Pessoas que estão no terminal: {', '.join(passageiros)}")

#     bool (aguardando)
#     if aguardando:
#         print(f"Voltando o {', '.join(aguardando)}")
#         aguardando.pop()
#     else:
#         print(f'\nFortwo chegou ao destino.\n\nTodos os passageiros estão no aguarde para partir:')


# pv = LevandoP('Chefe', 'Piloto')
# sv = passageiromotorista('policial', 'Presidiário')
# tv = embarques('Piloto', 'Oficial1')
# ql = embarques('Piloto', 'Oficial2')
# quintal = embarques('Chefe', 'Comissária1')
# sl = embarques('Chefe', 'Comissária2')
# setimal = passageiromotorista('Piloto', 'Chefe')

# print(f"Todos os passageiros - {', '.join(passageiros)}")