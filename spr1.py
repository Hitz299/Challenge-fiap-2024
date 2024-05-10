import time;
import random;
# Foi importada a biblioteca "time" para permitir execução de códigos que envolvam manipulação
# de tempo, como fazer o usuário esperar para realizar novas tentativas de login.
# a Biblioteca random foi importada para permitir algumas simulações de cenários reais, como por exemplo,
# simular possíveis defeitos que poderiam ser mostrados ao usuário quando for realizada a inspeção

# Para casos em que o usuário terá que realizar uma escolha no menu interativo e o mesmo digitar uma
# entrada inválida
def erro_entrada(entrada):
    while entrada != 1 and entrada != 2:
        entrada = int(input(f"Entrada inválida\n"))
    return entrada

def entrada_valor():
    entrada = input(f"\n")
    return entrada

def entrada_valor_numerico():
    entrada = int(input(f"\n"))
    return entrada

def quant_caracteres(entrada):
   while len(entrada) < 8 :
        print(f"\nEntrada inválida, você deve informar uma senha com no mínimo 8 caracteres: ")
        entrada = entrada_valor()
   return entrada

def menu():
    print(f"\nO usuário foi direcionado para a página inicial do projeto")

    print(f"Na tela inicial, o usuário pode escolher entre:\n"
                +f"1 - Adicionar novos veículos a plataforma\n"
                +f"2 - Acessar informações dos veículos que ele já possui\n")
    escolha = entrada_valor_numerico()
    escolha = erro_entrada(escolha)
    return escolha

def funcionalidades(escolha):
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
            print(f"Qual veículo você deseja selecionar?\n"
                                +f"1 -> {carros_usuario[0]}\n"+
                                f"2 -> {carros_usuario[1]}\n\n")
            escolha_veiculo = entrada_valor_numerico()

            escolha_veiculo = erro_entrada(escolha_veiculo)

            if escolha_veiculo == 1:
                    carro_escolhido = carros_usuario[0]

            elif escolha_veiculo == 2:
                    carro_escolhido = carros_usuario[1]

            print(f"Você selecionou o veículo {carro_escolhido}")

            print(f"Qual serviço você gostaria de acessar para seu veículo?\n"
                                +f"1 -> Localizar veículo\n"
                                +f"2 -> Inspecionar erros do veículo\n\n")

            escolha = entrada_valor_numerico()

            escolha = erro_entrada(escolha)
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
                 # lista dos possíveis erros que um usuário poderia ter
                 erros = ["Nenhum", "embreagem", "correia", "cambio", "motor"]
                 # variável para pegar itens (erros) aleatórios da lista de erros.
                 # foi subtraído o valor 2 da lista para evitar que seja sorteado um
                 # index inexistente na lista
                 numerosErros = random.randint(0, len(erros) -2)
                 # se o elemento "nenhum" entrar para o "numeroErros" de primeira, significa que
                 # um possível erro já foi identificado, então o item "nenhum" será retirado da lista
                 # e serão levados em consideração apenas os elementos restantes, que são os erros de fato
                 if erros[numerosErros] != erros[0]:
                    # retirando a possibilidade de "nenhum" erro
                    erros.pop(0)
                    # lista dos erros encontrados no veículo do usuário
                    errosList = []
                    # variável que servirá para guardar o endereço dos erros que serão
                    # adicionados a "errosList" 
                    errosIndex = 0
                    # cada erro que for sorteado para "numerosErros" será adicionado a lista de erros
                    for i in (range(numerosErros)):
                        errosIndex = random.randint(0, numerosErros)
                        errosList.append(erros[errosIndex])
                        # Para evitar a repetição um mesmo erro
                        erros.pop(errosIndex)
                        numerosErros -= 1

                    print(f"Foram encontrados problemas com os seguintes componentes"
                          +f"de seu veículo:\n{errosList}")

                    print(f"Deseja obter o valor do orçamento?\n"
                                        "1 -> Sim\n2 -> Não\n")

                    escolha = entrada_valor_numerico()

                    escolha = erro_entrada(escolha)

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
                              +f"veículo ficou: {valor_orcamento: .2f}R$")

                    elif escolha == 2:
                        print(f"O usuário foi direcionado para a tela inicial")                

                 else:
                    print(f"O seu veiculo está perfeito\nSessão finalizada")

print(f"Vamos criar uma conta para você!\n Comece seu cadastro\n"
              +"Informando seu E-mail: ")

email_criar_conta = entrada_valor()

print(f"Ok, Agora crie uma senha forte para proteger sua conta\n"
              +"Sua senha deve conter no mínimo 8 caracteres: ")

senha_criar_conta = entrada_valor()

senha_criar_conta = quant_caracteres(senha_criar_conta)

print(f"\nO usuário foi direcionado para a tela de login\n\n"
      +f"1 -> caso tenha esquecido a senha\n" + 
      f"Qualquer outro valor numérico -> caso queira prosseguir com o login: ")

print(f"\nDigite sua escolha: ")
escolha = entrada_valor_numerico()

if escolha == 1:

    print(f"\n Informe seu email para que possamos enviar "
                            +"o código de verificação: ")    

    email_recupecao = entrada_valor()    

    if email_criar_conta == email_recupecao:
        codigo = int(random.randrange(10000, 99999))
        # Simulando o código de verificação sendo enviado para o email do usuário
        print(f"\nO código de verificação é:\n{codigo}")
    
        print(f"\nInforme o código de verificação: ")
        codigo_usuario = entrada_valor_numerico()
    
        while codigo_usuario != codigo:
            print(f"\n\nO Código informado está errado\n")
            codigo = int(random.randrange(10000, 99999))
        
            print(f"O código de verificação é:\n{codigo}")
        
            codigo_usuario = entrada_valor_numerico()
            
        if codigo == codigo_usuario:
            print(f"\nDigite uma nova senha: ")
            senha_criar_conta =  entrada_valor()
            senha_criar_conta = quant_caracteres(senha_criar_conta)
    else:
        print(f"Email inválido, você foi desconectado")
        exit()

print(f"\nInforme seu email: ")
email_login = entrada_valor()
print(f"\nInforme sua senha: ")
senha_login = entrada_valor()
contador_tentativas = 3

# Se alguma das credenciais estiver errada, o usuário terá seu acesso negado, porém
# poderá tentar novamente. Caso insira as credenciais erradas 3 vezes seguidas, ele precisará
# esperar 10 segundos para tentar novamente
while senha_login != senha_criar_conta or email_criar_conta != email_login:

    contador_tentativas -= 1
    print(f"Email ou senha estão incorretos, por favor, preencha os campos novamente\n"
            +f"Você ainda possui {contador_tentativas} tentativas")
    
    if contador_tentativas <= 0:
        print(f"Você atingiu a quantidade limite de tentativas, tente novamente após 10 segundos.")
        time.sleep(10.0)
        contador_tentativas = 3
    
    email_login = input(f"\nInforme seu email: ")
    senha_login = input(f"\nInforme sua senha: ")

if email_criar_conta == email_login and senha_criar_conta == senha_login:
    print(f"Acesso liberado")

sair = False

while sair == False:
    escolha = menu()

    funcionalidades(escolha)
    
    print("\nVocê deseja continuar na plataforma?\n" +
          "1 -> Sim\n2-> Não")
    
    escolha = entrada_valor_numerico()
    erro_entrada(escolha)
    
    if escolha == 2:
        print("Até a próxima!")
        sair = True