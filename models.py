from sqlalchemy import Column, column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

#Ajuste as informações de acordo com o seu banco de dados local
USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "testes"
PORT = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()

class Cadastro(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key = True)
    usuario = Column(String(15))
    email = Column(String(50))
    senha = Column(String(100))

Base.metadata.create_all(engine)