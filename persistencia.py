import json

def salvar_dados(banco):
    dados = [conta.dados_para_dict() for conta in banco.contas]
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)

def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []