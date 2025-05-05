from utils.db import conectar, criar_tabela


def salvar_sessao(usuario_id):
    with open("session.txt", "w") as f:
        f.write(str(usuario_id))
def carregar_sessao():
    try:
        with open("session.txt", "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return None
def limpar_sessao():
    import os
    if os.path.exists("session.txt"):
        os.remove("session.txt")
