import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# 1. Cria a tabela (agora com o parêntese e aspas fechados corretamente)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# 2. Insere o admin (usando OR IGNORE para não duplicar caso já exista)
cursor.execute('''
INSERT OR IGNORE INTO usuarios (nome, senha) VALUES ('admin', 'admin123')
''')

conexao.commit()
conexao.close()

print("Banco de dados criado e usuário admin adicionado com sucesso!")