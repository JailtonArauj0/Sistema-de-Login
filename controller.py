from sqlalchemy import Column, ColumnDefault, column, ForeignKey, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import hashlib
from models import Cadastro

#Ajuste as informações de acordo com o seu banco de dados local
USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "login2"
PORT = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

def RetornaSession():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(engine)
    session = Session()
    return session

class CadastroController():
    def cadastrar(self, usuario: str, email: str, senha: str):
        session = RetornaSession()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        verificacao_email = session.query(Cadastro).filter_by(email = email).all()

        
        if len(verificacao_email) == 0:
            novo_usuario = Cadastro(usuario= usuario, email= email, senha= senha)
            session.add(novo_usuario)
            session.commit()
            return 1 #Usuário cadastrado com sucesso.
        else:
            return 2 #Email já cadastrado no sistema.

class LoginController():
    def login(self, email:str, senha:str):
        session = RetornaSession()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        verificacao_email = session.query(Cadastro).filter_by(email = email).all()
        verificacao_senha = session.query(Cadastro).filter_by(senha = senha).all()

        if len(verificacao_email) > 0:
            if len(verificacao_senha) > 0:
                return 0
            else:
                return 4 #Senha incorreta.

        else: 
            return 3 #Email não encontrado.

