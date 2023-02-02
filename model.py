from sqlalchemy import create_engine, Column, Integer, String, BINARY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SESSÂO QUE INICIA A CONEXÃO COM O BANCO DE DADOS MySQL
USERS = "root" #Usuario ADMIN do Banco de dados
PASSWORD = "" #Senha ADMIN do Banco de dados
HOST = "localhost" #Local Hospedado do Banco de dados
BANK = "projetologin" #Nome Banco de dados
PORT = "3306" #Porta onde o Banco de dados está hospedada
CONNECT = f"mysql+pymysql://{USERS}:{PASSWORD}@{HOST}:{PORT}/{BANK}" #String de Conexão
engine = create_engine(CONNECT, echo=False) 
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#CRIA UMA TABELA NO BANCO DE DADOS COM AS RESPECTIVAS COLUNAS
class Registros(Base):
    __tablename__ = "registros" 

    id = Column(Integer, primary_key=True, autoincrement=True) 
    nome = Column(String(50)) 
    email = Column(String(40), primary_key=True) 
    senha = Column(BINARY(32)) 

Base.metadata.create_all(engine) 
