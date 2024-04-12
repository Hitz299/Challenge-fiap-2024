import time;
import random;

email_criar_conta = input("Vamos criar uma conta para você!\n Comece seu cadastro\n"
              +"Informando seu E-mail: ")

senha_criar_conta = input("Ok, Agora crie uma senha forte para proteger sua conta\n"
              +"Sua senha deve conter no mínimo 8 caracteres: ")

while len(senha_criar_conta) < 8 :
    senha_criar_conta = input("\nSua senha deve contar mais de 8 caracteres: ")
    
print("\nO usuário foi direcionado para a tela de login\n\n"
      +"1 -> caso tenha esquecido a senha\n" + 
      "Qualquer outro valor numérico -> caso queira prosseguir com o login")

escolha = int(input("\nDigite sua escolha: "))

if escolha == 1:
    email_recupecao = input("\n Informe seu email para que possamos enviar"
                            +"o código de verificação: ")    
    
    codigo = int(random.randrange(10000, 99999))
    # Simulando o código de verificação sendo enviado para o email do usuário
    print(f"O código de verificação é:\n{codigo}")
    
    codigo_usuario = int(input("Informe o código de verificação: "))
    
    while codigo_usuario != codigo:
            print("\n\nO Código informado está errado\n")
            codigo = int(random.randrange(10000, 99999))
        
            print(f"O código de verificação é:\n{codigo}")
        
            codigo_usuario = int(input("Informe o código de verifição: "))
            
    if codigo == codigo_usuario:
        senha_criar_conta = input("Digite uma nova senha: ")
    
email_login = input("\nInforme seu email: ")
senha_login = input("\nInforme sua senha: ")
contador_tentativas = 3



while senha_login != senha_criar_conta or email_criar_conta != email_login:

    contador_tentativas -= 1
    print("Email ou senha estão incorretos, por favor, preencha os campos novamente\n"
            +f"Você ainda possui {contador_tentativas} tentativas")
    
    
    if contador_tentativas <= 0:
        print("Você atingiu a quantidade limite de tentativas, tente novamente após 60 segundos.")
        time.sleep(60.0)
    
    email_login = input("\nInforme seu email: ")
    senha_login = input("\nInforme sua senha: ")

    

if email_criar_conta == email_login and senha_criar_conta == senha_login:
    print("Acesso liberado")
    
print("\nO usuário foi direcionado para a página inicial do projeto")

escolha = int(input("Na tela inicial, o usuário pode escolher entre:\n"
                +"1 - Adicionar novos veículos a plataforma\n"
                +"2 - Acessar informações dos veículos que ele já possui\n\n"))

while escolha != 1 and escolha != 2:
    escolha = int(input("\nEntada inválida, escolha uma das opções anteriores: "))
    
      
match escolha:
    case 1:
        chassi = input("\nInforme o chassi do veículo: ")
        placa =  input("\nInforme a placa do veículo: ")

        carros = ("Fiat uno", "Ferrari", "Porshe", "Fiat toro", "Hyundai HB20",
                "Volkswagen Gol", "Nissan Versa")
           
        quantCarro = len(carros)
        print(quantCarro)
        veiculo_usuario = random.randrange(0,quantCarro-1)
        print(f"Ok, seu {carros[veiculo_usuario]} foi Adicionado")
        
    case 2:
        print(f"{carros}")