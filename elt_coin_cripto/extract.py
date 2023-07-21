#############################################################################
###################### Processo de Extração de Dados ########################
#############################################################################
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Session

def extract_data(iniciar, terminar, moeda, key, url):
    
    # definindo limite de dados da 'API'
    parametros = {
        'start': iniciar,
        'limit': terminar,
        'convert': moeda,
    } 

    acesso = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(acesso)

    try:
        resposta = session.get(url, params=parametros)
        datas = json.loads(resposta.text)
        print(datas)    
        print("\n")

    except (ConnectionError, Timeout, TooManyRedirects) as error:
        print(error)
    
    return datas

