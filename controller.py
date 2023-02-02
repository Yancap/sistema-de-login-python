from dal import DaoLogin, DaoRegister
from hashlib import sha256

# Sessão responsavel pelo Grosso do Back-End da Aplicação: Operações, Validações, Registro, Login, Criptografia 

class Controller():

    DBR = DaoRegister()
    DBL = DaoLogin()

    #Função que verifica o tamanho de cada dado
    @classmethod
    def isValidLength(cls, value, typeof):

        if typeof == "nome":

            return "valid" if len(value) <= 50 else "invalid"

        elif typeof == "email":

            return "valid" if len(value) <= 40 else "invalid"

        elif typeof == "senha":

            return "valid" if len(value) <= 32 else "invalid"

    #Função que verifica se o Email digitado é valido
    @classmethod
    def isValidEmail(cls, email):
        if "@" in email and "." in email:
            return "valid"
        return "invalid"
    #Função que verifica se a Senha atende aos requisitos básicos de Conter Mínimo de 8 Dígitos,
    #Números, Caracteres Especiais e Letra Maiúscula
    
    @classmethod
    def isValidPassword(cls, senha):
        control = ""

        if len(senha) < 8:

            return "invalid"

        for p in senha:

            if p in "@#$&%":
                control += "2"

            elif p in "1234567890":
                control += "1"

            elif p in "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ":
                control += "0"

        if "2" in control and "1" in control and "0" in control:
            return "valid"

        return "invalid"
    
    #função que verifica se o Email Existe ou não
    @classmethod
    def emailIsExisting(cls, email):
        __emails = cls.DBL.selectEmails()
        if email in __emails:
            return 'exist'
        return 'noexist'
    
    #Função que Criptografa a Senha
    @classmethod
    def criptPassword(cls, senha):
        hashPassword = sha256(senha.encode()).digest()
        print(type(hashPassword))
        return hashPassword

    #Função que salva o Registro do Usuário
    @classmethod
    def register(cls, nome, email, senha):
        cls.DBR.saveData(nome, email, cls.criptPassword(senha))

    #Função que Valida o Login e a Senha
    @classmethod
    def login(cls, email, senha):
        cls.__Data = cls.DBR.filterData("email", email)[0]
        
        if cls.__Data.senha != sha256(senha.encode()).digest():
            return "password_invalid"
        return cls.DBR.filterData("senha", sha256(senha.encode()).digest())[0]

