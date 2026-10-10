from banco import Banco
from persistencia import carregar_dados, salvar_dados
from operacoes import criar_conta

banco = Banco()

dados = carregar_dados()

for conta_dict in dados:
    conta = banco.criar_conta(
        conta_dict['titular'],
        conta_dict['saldo'])
    conta.extrato = conta_dict['extrato']

def exibir_menu_incial():
    escolha_usuario = int(input('''
    Digite a opção que deseja realizar:
    1 - Criar conta
    2 - Depositar
    3 - Sacar
    4 - Transferir
    5 - Exibir extrato
    6 - Listar contas
    0 - Sair
    '''))
    return escolha_usuario

def inciar_programa():
    while True:
        try:
            escolha = exibir_menu_incial()
            if 7 >escolha>= 0: 
                if escolha == 1:
                    criar_conta(banco)
                    salvar_dados(banco)
                    print('Conta criada e salva com sucesso!')
                elif escolha == 2:
                   pass 
                    
            else:
                print('Digite uma opção entre 0 e 6')
        except ValueError:
            print('Digite uma opção valida')


inciar_programa()


