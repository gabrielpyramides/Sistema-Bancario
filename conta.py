class Conta:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = float(saldo)

    def __str__ (self):
        return f'Títular: {self.titular} | Saldo: R${self.saldo}'

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')