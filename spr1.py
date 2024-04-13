import time;
import random;
'''
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
        
            codigo_usuario = int(input(f"Informe o código de verifição: "))
            
    if codigo == codigo_usuario:
        senha_criar_conta = input("Digite uma nova senha: ")
    
email_login = input(f"\nInforme seu email: ")
senha_login = input(f"\nInforme sua senha: ")
contador_tentativas = 3



while senha_login != senha_criar_conta or email_criar_conta != email_login:

    contador_tentativas -= 1
    print("Email ou senha estão incorretos, por favor, preencha os campos novamente\n"
            +f"Você ainda possui {contador_tentativas} tentativas")
    
    
    if contador_tentativas <= 0:
        print("Você atingiu a quantidade limite de tentativas, tente novamente após 10 segundos.")
        time.sleep(10.0)
    
    email_login = input(f"\nInforme seu email: ")
    senha_login = input(f"\nInforme sua senha: ")

    

if email_criar_conta == email_login and senha_criar_conta == senha_login:
    print(f"Acesso liberado")
    
'''
print("\nO usuário foi direcionado para a página inicial do projeto")

escolha = int(input(f"Na tela inicial, o usuário pode escolher entre:\n"
                +f"1 - Adicionar novos veículos a plataforma\n"
                +f"2 - Acessar informações dos veículos que ele já possui\n\n"))

while escolha != 1 and escolha != 2:
    escolha = int(input(f"\nEntada inválida, escolha uma das opções anteriores: "))
    
      
match escolha:
    # Funcionalidade 1 -> Adicionar veículo
    case 1:
        chassi = input(f"\nInforme o chassi do veículo: ")
        placa =  input(f"\nInforme a placa do veículo: ")

        carros = (f"Fiat uno", "Ferrari", "Porsche", "Fiat toro", "Hyundai HB20",
                "Volkswagen Gol", "Nissan Versa")
           
        print(f"Ok, seu {random.choice(carros)} foi Adicionado")
        
    # Funcionalidades 2 e 3
    case 2:
        carros_usuario = ("Ferrari", "Porshe")
        carro_escolhido: str
        escolha_veiculo = int(input(f"Qual veículo você deseja selecionar?\n"
                            +f"1 -> {carros_usuario[0]}\n"+
                            f"2 -> {carros_usuario[1]}\n\n"))
        
        if escolha == 1:
                carro_escolhido = carros_usuario[0]
               
        elif escolha == 2:
                carro_escolhido = carros_usuario[1]
               

        print(f"Você selecionou o veículo {carro_escolhido}")

        escolha = int(input(f"Qual serviço você gostaria de acessar para seu veículo?\n"
                            +"1 -> Localizar veículo\n"
                            +"2 -> Inspecionar erros do veículo\n\n"))
        
        # Funcionalidade 2 -> Localizar veículo
        if escolha == 1:
            if escolha_veiculo == 1:
                print(f"Seu veículo foi localizado em:\nBrasil - SP - Piraporinha - Bairro do limoeiro - Rua da Goiaba")
            elif escolha_veiculo == 2:
                print(f"Seu veículo foi localizado em:\nBrasil - SP - São Paulo - Capão redondo - Oficina de desmanche de veículos (clandestino)")
            else:
                 print(f"Escolha uma opção válida")
        
        # Funcionalidade 3 -> Inspecionar erros do veículo
        elif escolha == 2:
             erros = ["Nenhum", "embreagem", "correia", "cambio", "motor"]
             numerosErros = random.randint(0, len(erros) - 1)
             
             if erros[numerosErros] != erros[0]:
                erros.pop(0)
                errosList = []
                errosIndex = 0
                for i in (range(numerosErros)):
                    errosIndex = random.randint(0, numerosErros)
                    errosList.append(erros[errosIndex])
                    erros.pop(errosIndex)
                    numerosErros -= 1
                
                print(errosList)
                
                escolha = int(input(f"Deseja obter o valor do orçamento?\n"
                                    "1 -> Sim\n2 -> Não\n"))
                
                while escolha != 1 and escolha != 2:
                    escolha = int(input(f"Entrada inválida!\nTente novamente\n\n"))
                if escolha == 1:
                    valor_orcamento = 0.0
                    if errosList.__contains__("embreagem"):
                        valor_orcamento += 400.00
                    if errosList.__contains__("correia"):
                        valor_orcamento += 500.00
                    if errosList.__contains__("cambio"):
                        valor_orcamento += 3500.00
                    if errosList.__contains__("motor"):
                        valor_orcamento += 4000.00
                        
                    print(f"\n\nO orçamento para reparo completo do seu\n"
                          +f"veículo fiou: {valor_orcamento: .2f}R$")
                    
                elif escolha == 2:
                    print(f"O usuário foi direcionado para a tela inicial")
                
                
             else:
                print(f"O seu veiculo está perfeito")
                
            
                
        