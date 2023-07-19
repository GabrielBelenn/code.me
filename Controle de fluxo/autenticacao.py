login_correto = "gabriel@mail.com"
senha_correta = "mail2023"

while True:
    login = input("Insira seu login:\n")
    if login != login_correto:
        print("Nome de usuário não existente")
        input("Digite o login correto:\n")
        input("Digite o login correto:\n")
        input("Digite o login correto:\n")
        if login != login_correto:
            print("Tente novamente mais tarde...")
            break

    senha = input("Insira sua senha:\n")
    if senha != senha_correta:
        print("Senha incorreta!")
        input("Digite sua senha correta, você tem três chances:\n")
        input("Digite sua senha correta, você tem três chances:\n")
        input("Digite sua senha correta, você tem três chances:\n")
        if senha != senha_correta:
            print("Tente novamente mais tarde...")
            break


    if login == login_correto and senha == senha_correta:
        print("Autenticação bem sucedida...")
        print("Bem vindo a sua conta, você tem novas mensagens!")
        break
