from conta import Conta

class Banco():
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo = 0):
        conta = Conta(titular, saldo)
        self.contas.append(conta)
        return conta
    
    def listar_contas(self):
        for conta in self.contas:
            print(conta)            