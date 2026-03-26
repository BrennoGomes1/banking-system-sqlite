# 💰 Sistema Bancário com SQLite

## 📌 Descrição

Este projeto é um sistema simples de gerenciamento de contas bancárias desenvolvido em Python utilizando SQLite como banco de dados.

O sistema permite criar contas, armazenar dados de clientes e consultar informações financeiras básicas.

---

## 🧠 Funcionalidades

* Criação de tabela de contas bancárias
* Inserção de dados (titular, saldo e CPF)
* Evita duplicidade de CPF (UNIQUE)
* Consulta de contas cadastradas
* Exibição formatada de saldo

---

## 🗂 Estrutura do Banco de Dados

### Tabela: contas_bancarias

| Campo   | Tipo    | Descrição           |
| ------- | ------- | ------------------- |
| id      | INTEGER | Identificador único |
| titular | TEXT    | Nome do titular     |
| saldo   | FLOAT   | Saldo da conta      |
| cpf     | TEXT    | CPF único           |

---

## 🛠 Tecnologias Utilizadas

* Python 3
* SQLite3

---

## 🚀 Como executar o projeto

1. Clone o repositório:
   git clone https://github.com/BrennoGomes1/banking-system-sqlite.git

2. Acesse a pasta:
   cd banking-system-sqlite

3. Execute o projeto:
   python main.py](https://github.com/BrennoGomes1/banking-system-sqlite.git)

---

## 💻 Exemplo de saída

---

Titular: Brenno<br>
Saldo: R$ 123.00<br>
-------------------

---

## 📚 O que foi praticado

* Manipulação de banco de dados com SQLite
* Execução de comandos SQL via Python
* Criação de tabelas e constraints (UNIQUE)
* Boas práticas com commit() e conexões

---

## 🔒 Melhorias futuras

* Interface gráfica (GUI)
* Sistema de depósito e saque
* Validação de CPF
* Integração com API

---

## 👨‍💻 Autor

Brenno Gomes

---

## 📎 Observações

Projeto desenvolvido para fins de estudo e prática de banco de dados e Python.
