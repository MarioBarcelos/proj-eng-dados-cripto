#############################################################################
############### Configurações de Banco de Dados e a API #####################
#############################################################################

# acesso ao banco de dados 'postgresql' criado na aws
db_usuario='postgres'
db_senha='#msbp123'
db_hostname='ed-comerciomoedas.cisvuqjrzfih.us-east-2.rds.amazonaws.com'
db_port='5432'
db_nome='comercioMoedas'
tb_nome='moedas'

# quantidade de coins retornados por requisição e acesso a API
api_iniciar = '1'
api_terminar = '2'
api_key = '6ad243eb-ea9f-4ef9-86c1-eba246d583bf'
api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
api_moeda = 'USD'