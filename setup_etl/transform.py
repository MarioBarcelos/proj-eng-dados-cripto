#############################################################################
############# Processo de Validação e Agração dos Dados  ####################
#############################################################################
import pandas as pd
from extract import extract_data
import acess

all_data = extract_data(acess.api_iniciar,
                        acess.api_terminar,
                        acess.api_moeda,
                        acess.api_key,
                        acess.api_url)

def transform_data(*args,**kwargs):
    dados = all_data

    nome = []
    simbolo = []
    inserido_em = []
    atualizado_em = []
    preco = []
    volume_24h = []

    # condição para coletar os respectivos valores e inserir em cada lista
    # modelo amostra do tipo e extrutura dos dados em /estrutura_dados.json
    for coin in dados['data']:
        nome.append(coin['name'])
        simbolo.append(coin['symbol'])
        atualizado_em.append(coin['last_updated'])
        inserido_em.append(coin['date_added'])
        preco.append(coin['quote']['USD']['price'])
        volume_24h.append(coin['quote']['USD']['volume_24h'])

    # gerando um dicionário para transforma-lo em um DF 
    coins = {
        'nome': nome,
        'simbolo': simbolo,
        'preco': preco,
        'volume_24h': volume_24h,
        'atualizado_em': atualizado_em,
        'inserido_em': inserido_em,
    }
    # criando um DF com dados 'estruturados'
    dados = pd.DataFrame(coins, columns=['nome','simbolo','preco','volume_24h','atualizado_em','inserido_em'])
    #dados['index'] = dados.index
    #dados = dados[['index','nome','simbolo','preco','volume_24h','atualizado_em','inserido_em']]

    return dados