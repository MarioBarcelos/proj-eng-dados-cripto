#############################################################################
############# Carregamento de Dados para no Banco de Dados ##################
#############################################################################
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base # SQLAlchemy==1.4.49
from sqlalchemy.orm import sessionmaker
import acess

Base = declarative_base()

class In_Moedas(Base):
    """ Esta Classe tem como objetivo realizar o processo de carga no Banco de Dados """
    
    # Definindo o schema do Banco de Dados
    __tablename__ = acess.tb_nome # se usar a 'Base' como parametro essa agregação é obrigatória
    id = Column(Integer, primary_key=True) # obrigatório
    #index=Column(String)
    nome = Column(String)
    simbolo = Column(String)
    preco = Column(Float)
    volume_24h = Column(Float)
    atualizado_em = Column(Text)
    inserido_em = Column(Text)

    def iniciar():
        # Instrução para 'carregamento' de Dados no Banco de Dados
        conn = 'postgresql://'+ acess.db_usuario \
                                + ':' + acess.db_senha \
                                + '@' + acess.db_hostname \
                                + ':' + acess.db_port \
                                + '/' + acess.db_nome
        print(conn)
        construtor = create_engine(conn)
        Session = sessionmaker(bind=construtor)
        session = Session()
        Base.metadata.create_all(construtor)
        return session, construtor