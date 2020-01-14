import MySQLdb
print('='*50)

conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
cursor = conexao.cursor()

################################################ Tabela pessoa ##################################################################################

#Salvar pessoa
def salvar(conexao, cursor, nome, sobrenome, idade, endereco_id=None):
    if endereco_id == None:
        endereco_id = 'Null'
    cursor.execute(F"INSERT INTO pessoa (Nome, Sobrenome, Idade, Endereço_ID)VALUES('{nome}', '{sobrenome}', {idade}, {endereco_id})")
    conexao.commit()

# salvar(conexao, cursor, 'joije', 'jow', 78)

#Alterar pessoa
def alterar(conexao, cursor, id, nome, sobrenome, idade, endereco_id='NULL'):
    cursor.execute(f"UPDATE pessoa SET Nome='{nome}', Sobrenome='{sobrenome}', Idade={idade}, Endereço_ID={endereco_id} WHERE ID={id}")
    conexao.commit()

# alterar(conexao, cursor, 5, 'joije', 'jowWWWWWWWWW', 15)

#Deletar pessoa
def deletar(conexao, cursor, id):
    cursor.execute(f'DELETE FROM pessoa WHERE ID={id}')
    conexao.commit()

# deletar(conexao, cursor, 6)

########################################################## Tabela endereço ####################################################################

#Salvar endereço
def salvar_endereco(conexao, cursor, logradouro, numero, complemento='NULL'):
    cursor.execute(F"INSERT INTO endereço (Logradouro, Número, Complemento)VALUES('{logradouro}', {numero}, '{complemento}')")
    conexao.commit()

# salvar_endereco(conexao, cursor, 'Sem saída', 15, 'No final da rua')

#Alterar endereço
def alterar_endereco(conexao, cursor, id, logradouro, numero, complemento='NULL'):
    cursor.execute(f"UPDATE endereço SET Logradouro='{logradouro}', Número={numero}, Complemento='{complemento}' WHERE ID={id}")
    conexao.commit()

# alterar_endereco(conexao, cursor, 4, 'Com saída', 50, 'Quase na saída')

#Deletar endereço
def deletar_endereco(conexao, cursor, id):
    cursor.execute(f'DELETE FROM endereço WHERE ID={id}')
    conexao.commit()

# deletar_endereco(conexao, cursor, 6)