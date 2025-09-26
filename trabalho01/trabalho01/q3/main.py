# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

from auth import auth_account

usuario = input("Usuário: ")
senha = input("Senha: ")

auth_account(usuario, senha)
