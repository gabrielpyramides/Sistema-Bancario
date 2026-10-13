from banco import Banco
from conta import Conta


def criar_conta(banco):
    numero = int(input('número da conta: '))
    titular = input('Títular: ')
    conta = banco.criar_conta(numero, titular)
    return conta

def depositar(banco):
    numero = int(input('Digite o número da conta que deseja depositar: '))
    conta = banco.buscar_conta(numero)
    valor = float(input('Digite o valor que dejesa depositar: '))
    Conta.depositar(conta, valor)

def saque(banco):
    pass
    

