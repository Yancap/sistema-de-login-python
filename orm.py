from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USERS = "root"
PASSWORD = ""
HOST = "localhost"
BANK = "projetologin"
PORT = "3306"

CONNECT = f"mysql+pymysql://{USERS}:{PASSWORD}@{HOST}:{PORT}/{BANK}"

engine = create_engine(CONNECT, echo=True) 
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Registros(Base):
    __tablename__ = "Registros" 

    id = Column(Integer, primary_key=True) 
    nome = Column(String(50)) 
    email = Column(String(40)) 
    senha = Column(String(12)) 

Base.metadata.create_all(engine)