#ORM
# ---- SqlAlchemy
#---- Instalação do framework
#--- pip3 install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip3 install mysql-connector-python

from Aula54.Dao.pessoa_dao import PessoaDao
from Aula54.Model.pessoa_model import PessoaModel

dao = PessoaDao()

p = PessoaModel

#p.nome = ''
#p.sobrenome = ''
#p.idade =
#p.id =
#print(dao.alterar(5))

print('-'*100)

#print(dao.deletar(6))
for p in dao.listar_todos():
    print(p)

print('-'*100)

#dao.buscar_por_id(5)