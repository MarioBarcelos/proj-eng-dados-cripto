#############################################################################
#################### Processo de Carga no Banco de Dados  ###################
#############################################################################
import pandas as pd 
from model_db import In_Moedas
from transform import transform_data

output_datas = transform_data()

def validar_dados(df: pd.DataFrame) -> bool:

    # checar se o DF está 'vazio'
    if df.empty:
        print('\nDataFrame vazio. Finalizando a execução!')
        return False
    
    # checar se há 'códigos da moeda' como 'null'
    if df.simbolo.empty:
        raise Exception("\nOs valores em 'simbolo' são nulos ou está vazio!")
    
    # checar se há 'preços' como 'null'
    if df.preco.empty:
        raise Exception("\nOs valores em 'preco' são nulos ou está vazio!")
    
    # checar se há 'datas' como 'null'
    if df.inserido_em.empty:
        raise Exception("\nOs valores em 'inserido_em' são nulos ou vazio!")
    
    return True

def load_data(nome_tabela, dados_df, con_db, construtor_db):

    # validando
    if validar_dados(dados_df):
        print('\nValidando os Dados...')
        print('\nDados válidos, iniciando o processo de carregamento.\n')
        print(dados_df.head(5))
        
        try:
            dados_df.to_sql(nome_tabela, construtor_db, index=False, if_exists='append')
            
        except:
            print('\nError, falha ao inserir os Dados no Banco de Dados')
    
    con_db.commit()
    con_db.close()
    print('\nDados carregados no Banco de Dados!')
    return con_db

# repassando a conexão e o construtor do Banco de Dados
get_con_db, construtor_con_db = In_Moedas.iniciar()

# carregando os dados no Baco de Dados
load_data('Moedas',
          output_datas, 
          get_con_db, 
          construtor_con_db)