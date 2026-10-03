class Conta:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = float(saldo)
        self.extrato = []


    def __str__ (self):
        return f'Títular: {self.titular} | Saldo: R${self.saldo}'

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f'Depósito: R${valor}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f'Saque: R${valor}')
        else:
            print('Saldo insuficiente!')

    def mostrar_extrato(self):
        print('=== EXTRATO ===')
        for operacao in self.extrato:
            print(operacao)