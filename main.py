import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

caminho_banco = os.path.join(BASE_DIR, "banco.db")

conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)""")


while True:
    print("\n--- Cadastro de Nova Conta ---")
    nome = input("Titular (ou 'sair' para ver todas): ")
    
    if nome.lower() == 'sair':
        break
        
    try:
        valor_inicial = float(input(f"Saldo inicial para {nome}: "))
        documento_cpf = input(f"CPF de {nome}: ")

        # Insere no banco de dados de forma segura
        cursor.execute("""
        INSERT INTO contas_bancarias (titular, saldo, cpf)
        VALUES (?, ?, ?)
        """, (nome, valor_inicial, documento_cpf))
        
        conexao.commit()
        print(" Conta salva no banco com sucesso!")
    except ValueError:
        print(" Erro: O saldo deve ser um número.")
    except Exception as e:
        print(f" Erro ao salvar: {e}")

cursor.execute("UPDATE contas_bancarias SET saldo = 1.50 WHERE id = 1")


cursor.execute("SELECT titular, saldo FROM contas_bancarias")
contas = cursor.fetchall()


print("-" * 20)
if not contas:
    print("Nenhuma conta encontrada.")
else:
    for conta in contas:
        titular, saldo = conta
        print(f"Titular: {titular}")
        print(f"Saldo: R$ {saldo:.2f}")
        print("-" * 20)


conexao.commit()
conexao.close()