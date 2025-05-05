# **Projeto 1**

Este é um sistema simples de **gestão de tarefas** com **cadastro de usuários**, **login**, e **CRUD de tarefas**, desenvolvido em Python. O projeto foi criado como parte de uma simulação de primeiro emprego como programador júnior, usando **SQLite** como banco de dados e **bcrypt** para segurança de senhas.

---

## 🚀 **Funcionalidades**

- **Cadastro de Usuário:** Permite criar novos usuários, com verificação de duplicação de e-mail.
- **Login e Logout:** Autenticação de usuários para acessar suas tarefas.
- **CRUD de Tarefas:**
  - **Criar:** O usuário pode adicionar novas tarefas.
  - **Listar:** Exibe todas as tarefas cadastradas.
  - **Atualizar:** Permite modificar título e descrição das tarefas.
  - **Deletar:** Exclui uma tarefa existente.
  
---

## 📦 **Tecnologias Utilizadas**

- **Python:** Linguagem principal de desenvolvimento.
- **SQLite:** Banco de dados local para persistência de dados.
- **bcrypt:** Biblioteca para segurança de senhas.
- **os:** Utilizado para gerenciar caminhos e arquivos do sistema.

---

## 🔧 **Instalação e Uso**

### Pré-requisitos

1. **Python** 3.x ou superior
2. **Bibliotecas Python**: Instalar as dependências necessárias com o comando:

```bash
pip install bcrypt sqlite3
