from sqlalchemy import Column, column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql


engine = create_engine("mysql+pymysql://root:@localhost/login2", echo=True)
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