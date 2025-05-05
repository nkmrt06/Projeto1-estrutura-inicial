from utils.db import criar_tabela
from controllers.auth import cadastrar_usuario, autenticar_usuario,buscar_usuario
from controllers.tasks import criar_tarefa, listar_tarefas, atualizar_tarefa, deletar_tarefa
from utils.session import salvar_sessao, carregar_sessao, limpar_sessao


def main():
    
    criar_tabela()
    usuario_id = carregar_sessao()
    usuario_logado = buscar_usuario(usuario_id) if usuario_id else None

    while True:
        if not usuario_logado:
            print("\n1 - Cadastrar\n2 - Login\n0 - Sair")
            op = input("Escolha: ")
            if op == "1":
                nome = input("Nome: ")
                email = input("Email: ")
                senha = input("Senha: ")
                cadastrar_usuario(nome, email, senha)
            elif op == "2":
                email = input("Email: ")
                senha = input("Senha: ")
                usuario_logado = autenticar_usuario(email, senha)
                if usuario_logado:
                    salvar_sessao(usuario_logado[0])  # Salva o ID do usuário
                else:
                    print("❌ Email ou senha incorretos.")

            elif op == "0":
                break
        else:
            print("\n1 - Criar tarefa\n2 - Listar tarefas\n3 - Atualizar tarefa\n4 - Deletar tarefa\n5 - Logout\n0 - Sair")
            op = input("Escolha: ")
            if op == "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                criar_tarefa(titulo, descricao, usuario_logado[0])
            elif op == "2":
                tarefas = listar_tarefas(usuario_logado[0])
                for t in tarefas:
                    print(f"{t[0]} - {t[1]}: {t[2]}")
            elif op == "3":
                tarefa_id = int(input("ID da tarefa a atualizar: "))
                titulo = input("Novo título: ")
                descricao = input("Nova descrição: ")
                atualizar_tarefa(tarefa_id, titulo, descricao)
            elif op == "4":
                tarefa_id = int(input("ID da tarefa a deletar: "))
                deletar_tarefa(tarefa_id)
            elif op == "5":
                usuario_logado = None
                limpar_sessao()
                print("Você foi desconectado.")
            elif op == "0":
                break    

main()