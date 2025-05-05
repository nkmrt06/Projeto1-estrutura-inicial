import sqlite3

def conectar():
    return sqlite3.connect('sistema.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            usuario_id INTEGER,        
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')    
    conn.commit()
    conn.close()