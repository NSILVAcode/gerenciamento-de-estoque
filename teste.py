import sqlite3

# Conecta apenas para ler os dados
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

print("Conteúdo atual da tabela:", usuarios)

conexao.close()