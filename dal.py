from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from model import Registros

#SESSÃO QUE PERMITE O ACESSO, CONEXÃO, ENVIO E REQUISIÇÕES NO BANCO DE DADOS

class DaoRegister():
    def __init__(self):
        #cria uma instancia que permite a conexão ao banco de dados
        USERS = "root"
        PASSWORD = ""
        HOST = "localhost"
        BANK = "projetologin"
        PORT = "3306"
        CONNECT = f"mysql+pymysql://{USERS}:{PASSWORD}@{HOST}:{PORT}/{BANK}" 
        engine = create_engine(CONNECT, echo=False) 
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def saveAllAlterations(self):
        #Salva e envia as alterações para o banco de dados
        self.session.commit()
    
    def saveData(self, nome, email, senha):
        #Salva o Registro do usuário na Camada intermediaria entre o Python e o banco de dados 
        data = Registros(nome=nome,email=email, senha=senha)
        self.session.add(data)
        self.saveAllAlterations() #Envia essas alterações ao banco de dados
    
    def loadData(self):
        #Retorna todos os dados da Tabela do Banco de Dados
        return self.session.query(Registros).all()

    def updateData(self, id, modify, value):
        #Função que atualiza valores de uma Coluna do Banco de Dados referente ao ID selecionado
        update = session.query(TabelaExemplo).filter(TabelaExemplo.id == id).all() 
        if modify == "nome":
            update[0].nome = value
        elif modify == "email":
            update[0].email = value
        elif modify == "senha":
            update[0].senha = value
        self.saveAllAlterations()
    def filterData(self, column, data):
        #Função que retorna a Linha do bancos de dados, com base em uma Coluna e o valor nela contido
        if column == "nome":
            return self.session.query(Registros).filter(Registros.nome == data)
        elif column == "email":
            return self.session.query(Registros).filter(Registros.email == data)
        elif column == "senha":
            return self.session.query(Registros).filter(Registros.senha == data)
        else:
            return self.session.query(Registros).filter(Registros.id == data)
    
class DaoLogin(DaoRegister):
    #Função que Retorna todos os Emails do Banco de dados
    def selectEmails(self):
        array = list()
        datas = self.session.query(Registros).all()
        for data in datas:
            array.append(data.email)
        return array
    
    