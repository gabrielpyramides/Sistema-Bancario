from banco import Banco
from conta import Conta


def criar_conta(banco):
    numero = int(input('número da conta: '))
    titular = input('Títular: ')
    conta = banco.criar_conta(titular, numero)
    print('Conta criada! ')
    return conta

def depositar(banco):
    numero = int(input('Digite o número da conta que deseja depositar: '))
    conta = banco.buscar_conta(numero)
    valor = float(input('Digite o valor que dejesa depositar: R$'))
    Conta.depositar(conta, valor)
    print('Depósito realizado!')

def sacar(banco):
    numero = int(input('Digite o número da conta que deseja sacar: '))
    conta = banco.buscar_conta(numero)
    valor = float(input('Digite o valor que deseja sacar: R$'))
    Conta.sacar(conta, valor)
    print('Saque realizado!')

def transferir(banco):
    numero = int(input('Digite o número da sua conta: '))
    conta = banco.buscar_conta(numero)
    numero_destino = int(input('Digite o número da conta que deseja transferir: '))
    destino = banco.buscar_conta(numero_destino)
    valor = float(input('Digite o valor que deseja transferir: R$'))
    Conta.transferir(conta,valor, destino)
    print('Transferência realizada!')
