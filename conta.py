class Conta:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = float(saldo)
        self.extrato = []


    def __str__ (self):
        return f'Títular: {self.titular} | Saldo: R${self.saldo}'

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        else:
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

    def transferir(self,valor, destino):
        if self.saldo >= valor:
            destino.saldo += valor
            self.saldo -= valor
            self.extrato.append(f'Transferência enviada: R${valor}')
            destino.extrato.append(f'Transferência recebida: R${valor}')
        else:
            print('Saldo insuficiente')

    def dados_para_dict(self):
        dados_para_dict = {'titular': self.titular, 'saldo' : self.saldo, 'extrato' : self.extrato}
        return dados_para_dict