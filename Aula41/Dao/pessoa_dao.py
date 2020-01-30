class PessoaDao:
    def list_all(sel):
        return 'Listando todos os dados da tabela'
    def get_by_id(self, id):
        return 'Listando o dado de id: {}' .format(id)

    def insert(self, pessoa):
        return 'Cadastrar uma pessoa'

    def update(self, pessoa):
        return 'Alterando uma pessoa'

    def remove(self, id):
        return 'Rempvendo a pessoa: {}' .format(id)