#ORM
# ---- SqlAlchemy
#---- Instalação do framework
#--- pip3 install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip3 install mysql-connector-python

from Aula54.Dao.pessoa_dao import PessoaDao

dao = PessoaDao()
pessoa = dao.list_all()
print(pessoa)
for p in pessoa:
    print(p)