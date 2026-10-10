from banco import Banco

def criar_conta(banco):
    titular = input('Títular: ')
    conta = banco.criar_conta(titular)
    return conta

