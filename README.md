# 🏦 Sistema Bancário em Python

Projeto desenvolvido em Python com foco na prática de Programação Orientada a Objetos (POO), modularização de código e persistência de dados utilizando arquivos JSON.

O sistema funciona por meio de um menu interativo no terminal, permitindo a criação e gerenciamento de contas bancárias, além de registrar as informações de forma permanente entre execuções do programa.

## 🚀 Funcionalidades

- Criar contas bancárias
- Realizar depósitos
- Realizar saques
- Transferir valores entre contas
- Consultar extrato
- Listar contas cadastradas
- Salvar dados automaticamente em arquivo JSON
- Carregar dados salvos ao iniciar o sistema

## 🛠️ Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- JSON
- Manipulação de arquivos
- Tratamento de exceções

## 📂 Estrutura do Projeto

```text
Sistema-Bancario/
│
├── banco.py
├── conta.py
├── operacoes.py
├── persistencia.py
├── main.py
└── dados.json
```

### Organização dos Arquivos

- **conta.py** → Classe responsável pelas contas bancárias e suas operações.
- **banco.py** → Gerencia o conjunto de contas cadastradas.
- **operacoes.py** → Contém as funções utilizadas pelo menu.
- **persistencia.py** → Responsável por salvar e carregar os dados.
- **main.py** → Ponto de entrada da aplicação.
- **dados.json** → Armazena as informações das contas.

## ▶️ Como Executar

### Clone o repositório

```bash
git clone https://github.com/gabrielpyramides/Sistema-Bancario.git
```

### Acesse a pasta do projeto

```bash
cd Sistema-Bancario
```

### Execute o programa

```bash
python main.py
```

## 💻 Exemplo de Utilização

```text
Digite a opção desejada:

1 - Criar conta
2 - Depositar
3 - Sacar
4 - Transferir
5 - Exibir extrato
6 - Listar contas
0 - Sair
```

## 📚 Conceitos Praticados

Durante o desenvolvimento deste projeto foram aplicados conceitos importantes de desenvolvimento Python:

- Programação Orientada a Objetos
- Classes e Objetos
- Encapsulamento
- Modularização
- Manipulação de listas e dicionários
- Persistência de dados
- Serialização JSON
- Tratamento de exceções
- Separação de responsabilidades

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte dos meus estudos em desenvolvimento backend com Python.

O principal objetivo foi consolidar conhecimentos fundamentais de programação, organização de código e modelagem orientada a objetos antes de avançar para tecnologias como APIs REST, FastAPI e bancos de dados relacionais.

## 🔮 Melhorias Futuras

- Integração com PostgreSQL
- API REST com FastAPI
- Testes automatizados com Pytest
- Interface Web
- Sistema de autenticação
- Cadastro completo de clientes

## 👨‍💻 Autor

**Gabriel Cândido Pyramides Pinheiro**

- GitHub: https://github.com/gabrielpyramides
- LinkedIn: https://www.linkedin.com/in/gabrielpyramides/

---

⭐ Caso tenha gostado do projeto, fique à vontade para deixar uma estrela no repositório.
