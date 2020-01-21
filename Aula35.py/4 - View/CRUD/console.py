import MySQLdb
print('='*50)

conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root')
cursor = conexao.cursor()

################################################ Tabela squads ##################################################################################

#Salvar nome do squad
def salvar(conexao, cursor, nome, descricao, membros, linguagem_Back_End, framework_Front_End):
    cursor.execute(F"INSERT INTO aulabd.squads (Nome, Descricao, Numero_de_membros, Linguagem_Back_End, Framework_Front_End)VALUES('{nome}', '{descricao}', {membros}, '{linguagem_Back_End}', '{framework_Front_End}')")
    conexao.commit()

salvar(conexao, cursor, 'Rush', 'Vem tranquilo', 4, 'Python', 'Angular')

#Alterar squad
def alterar(conexao, cursor, id, nome, descricao, membros, linguagem_Back_End, framework_Front_End):
    cursor.execute(f"UPDATE squads SET Nome='{nome}', Descrição='{descrição}', Número de membros={membros}, Linguagem Back End='{linguagem_Back_End}', Framework Front End='{framework_Front_End}' WHERE ID={id}")
    conexao.commit()

# alterar(conexao, cursor, 5, 'joije', 'jowWWWWWWWWW', 15)

#Deletar squad
def deletar(conexao, cursor, id):
    cursor.execute(f'DELETE FROM squads WHERE ID={id}')
    conexao.commit()

# deletar(conexao, cursor, 6)