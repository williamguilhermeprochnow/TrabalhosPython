# Pip3 install flask_mysqldb
# Referência ao Mysql

import MySQLdb
print('='*50)

conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
cursor = conexao.cursor()

#Pesquisar por pessoa
cursor.execute('SELECT * FROM pessoa')
pessoas = cursor.fetchall()
for p in pessoas:
    print(p)

#listar todas as pessoas
def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

#Pesquisar as pessoas pelo id
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}') ###### like vai seguir as letra de um provavel nome que vc n sabe direito ######
    pessoa = c.fetchone()
    print(pessoa)

conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
cursor = conexao.cursor()

#Listar_todos(cursor)
buscar_por_id(cursor, 2)





# print('='*50)