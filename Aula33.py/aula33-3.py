#--- Exportação dos métodos
# from pessoa_db import listar_todos
# from pessoa_converte import converter_tabela_dicionario
# from pessoa_exporte import exportar_txt

# lpt = listar_todos()
# lpd = converter_tabela_dicionario(lpt)
# exportar_txt(lpd)

#--- Exportação da classe

from aula33-4 import Pessoa

p1 = Pessoa()
print(p1)
p1 = Pessoa()
p1.id = 10
p1.nome = 'William'
print(p1.id)
p2 = Pessoa()
p2.id = 11
p2.nome = 'Guilherme'
print(p2.id)