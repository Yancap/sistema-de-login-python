from controller import Controller

#Sessão que Aparece para o Usuario

print("BEM VINDO AO LoginPy!")
toController = Controller()
print("\nDigite\n 1 - Registrar\n 2 - Login\n")
quest = str(input(" >> ")).lower()
if quest == "1" or quest == "registrar":
    try:
        #Sessão de Registro
        print("------------------------")
        print("--- AREA DE REGISTRO ---")
        print("------------------------")
        
        #Entrada de Dados
        nome = str(input("Digite seu Nome: "))
        email = str(input("\nDigite seu Email: "))

        #Verifica se o Email é valido ou se Ele é existente
        while toController.isValidEmail(email) == "invalid" or toController.emailIsExisting(email) == "exist":
            #Se o Email for invalido ou Existente, pede para o Usuario Digitar novamente
            print("\nEmail Existente" if  toController.emailIsExisting(email) == "exist" else "\nEmail Invalido!")
            email = str(input("Digite Novamente! >> "))

        #Recebe a Senha e verifica se ela é Valida
        print("\nDigite sua Senha\n OBS:\n")
        print(" - Deve conter um mínimo de 8 Caracteres\n - Deve conter pelo menos um Carácter Especial '@#$&%' \n - Deve conter números \n - Deve conter ao menos Uma letra Maiúscula\n")
        senha = str(input(" >> "))
        while toController.isValidPassword(senha) == "invalid":
            #Se a senha for invalida, pede que digite novamente e mostra os requisitos básicos da senha
            print("\nSenha Inválida\n Atenção as Observações:\n")
            print(" - Deve conter um mínimo de 8 Caracteres\n - Deve conter pelo menos um Carácter Especial '@#$&%' \n - Deve conter números \n - Deve conter ao menos Uma letra Maiúscula\n")
            senha = str(input("Digite Novamente >> "))

        #Finaliza o Registro e Salva no Banco de Dados
        toController.register(nome, email, senha)
        print("Registrado com Sucesso")
    except:
        print("Ocorreu um Error")

    #Pergunta se Deseja Logar, caso contrario fecha o programa
    print("\nDeseja se Logar? \n 1 - sim\n 2 - não\n")
    quest = str(input(" >> ")).lower()
    quest = 1
    if quest == "2" or quest == "nao" or quest == "não":
        print("Digite ENTER para sair")
        input(" >> ")
        exit()

#Sessão de Login
print("-------------------------")
print("----- AREA DE LOGIN -----")
print("-------------------------")

#Recebimento de Dados
email = str(input("\nDigite seu Email: "))
#Verifica se o Email digitado é valido ou se não existe
while toController.isValidEmail(email) == "invalid" or toController.emailIsExisting(email) == "noexist":
    #Se for invalido ou não existir, pede que ele digite novamente
    print("\nEmail Não Existente" if  toController.emailIsExisting(email) == "exist" else "\nEmail Invalido!")
    email = str(input("Digite Novamente! >> "))

print("\nDigite sua Senha\n")
senha = str(input(" >> "))
#Verifica se a Senha é correta, caso contrario, pede que ele digite novamente
Login = toController.login(email, senha)
while Login == "password_invalid":
    print("Senha incorreta!")
    senha = str(input("Digite Novamente >> "))
    
print("Login efetuado com sucesso!\n Seja Bem-Vindo(a)", Login.nome)