from conta import Conta

class Banco():
    def __init__(self):
        self.contas = []

    def criar_conta(self,numero, titular, saldo = 0):
        conta = Conta(numero, titular, saldo)
        self.contas.append(conta)
        return conta
    
    def listar_contas(self):
        for conta in self.contas:
            print(conta)   

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == int(numero):
               return conta

        return None