from Aula60.ForTwo.r2.local import Local
class Fortwo:
    def __init__(self):
        self.__pessoas_permitidas = ['piloto', 'chefe de serviço','policial']
        self.__motorista = ''
        self.__passageiro = ['presidiário', 'comissario1', 'comissario2', 'oficial1', 'oficial2']

    def set_motorista(self, pessoa, tripulantes):
        # if pessoa in self.__pessoas_permitidas:
        #     self.__motorista = pessoa
        if tripulantes in self.__passageiro:
            self.__passageiro = tripulantes
            return True
        return False

    def get_motorista(self):
        return self.__motorista

    def set_passageiro(self, pessoa, tripulantes):
        # if self.__valida_regra_passageiro__(pessoa):
        #     self.__passageiro = pessoa
        if self.__valida_passageiro__(tripulantes):
            self.__motorista = tripulantes
            return True
        return False

    def get_passageiro(self):
        return self.__passageiro
        return self.__motorista

    def __valida_regra_passageiro__(self, pessoa) -> bool:
        if self.__motorista == 'policial':
            if pessoa == 'presidiário':
                return True
        elif self.__motorista == 'piloto':
            if pessoa != 'comissário1' and pessoa != 'comissário2' and pessoa != 'presidiário':
                return True
        elif self.__motorista == 'chefe de serviço' :
            if pessoa != 'oficial1' and pessoa != 'oficial2' and pessoa != 'presidiário':
                return True
        return False

    def __valida_passageiro__(self, tripulantes) -> bool:
        if self.__passageiro == 'presidiário':
            if tripulantes == 'policial':
                return True
        elif self.__passageiro == 'comissario1' and self.__passageiro == 'comissario2':
            if tripulantes == 'chefe de serviço' and tripulantes == 'policial':
                return True
        elif self.__passageiro == 'oficial1' and self.__passageiro == 'oficial2':
            if tripulantes == 'policial' and tripulantes == 'piloto':
                return True
        return False

    def viagem(self, origem:Local, destino):
        print(f"Saindo do {origem}")
        print('Iniciando a viagem...')
        print(f'motorista: {self.__motorista}')
        print(f'passageiro: {self.__passageiro}')
        print(f"Chegando no {destino}")
        print('Finalizando a viagem ...')
        print(f'{self.__motorista} e {self.__passageiro} descem no {destino}')
        print(f'origem: {origem.get_pessoas()}')
        print(f'destino: {destino.get_pessoas()}')