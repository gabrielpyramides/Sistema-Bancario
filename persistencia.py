import json

def salvar_dados(contas):
    with open('dados.json', 'w') as arquivo:
        json.dump(contas, arquivo)

def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []