def auth_account(user, password):
    usuarios = {
        "admin": "1234",
        "joao": "senha123",
        "maria": "abc@2024"
    }

    if usuarios.get(user) == password:
        return print("Autenticação bem-sucedida!")
    else:
        return print("Usuário ou senha incorretos.")
