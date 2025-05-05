from utils.db import conectar

def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    
   
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    usuario_existente = cursor.fetchone()
    
    if usuario_existente:
        return False  
    
    
    
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
    conn.commit()
    
    return True  

def autenticar_usuario(email, senha):   
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()
    
    if usuario:
        return usuario  
    
    return False

def buscar_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
    usuario = cursor.fetchone()
    
    return usuario  