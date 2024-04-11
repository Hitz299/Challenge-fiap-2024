email_criar_conta = input("Vamos criar uma conta para você!\n Comece seu cadastro\n"
              +"Informando seu E-mail: ")

senha_criar_conta = input("Ok, Agora crie uma senha forte para proteger sua conta\n"
              +"Sua senha deve conter no mínimo 8 caracteres: ")

while len(senha_criar_conta) < 8 :
    senha_criar_conta = input("\nSua senha deve contar mais de 8 caracteres: ")
    
print("O usuário foi direcionado para a tela de login")

email_login = input("\nInfome seu email: ")
senha_login = input("\nInfome sua senha: ")
contador_tentativas = 3

while senha_login != senha_criar_conta or email_criar_conta != email_login:
    contador_tentativas -= 1
    print("Email ou senha estão incorretos, por favor, preencha os campos novamente\n"
          +f"Você ainda possui {contador_tentativas} tentativas")
    
    email_login = input("\nInfome seu email: ")
    senha_login = input("\nInfome sua senha: ")

    if contador_tentativas <= 0:
        print("Você atingiu a quantidade limite de tentativas, tente novamente após 60 segundos.")

if (email_criar_conta == email_login and senha_criar_conta == senha_login):
    print("Acesso liberado")