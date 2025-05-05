from utils.db import conectar

def criar_tarefa(titulo, descricao, usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO tarefas (titulo, descricao, usuario_id) VALUES (?, ?, ?)", (titulo, descricao, usuario_id))
    conn.commit()
    
    return True 

def listar_tarefas(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tarefas WHERE usuario_id = ?", (usuario_id,))
    tarefas = cursor.fetchall()
    
    return tarefas


def atualizar_tarefa(tarefa_id, titulo, descricao):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?", (titulo, descricao, tarefa_id))
    conn.commit()
    
    return True

def deletar_tarefa(tarefa_id):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    
    return True