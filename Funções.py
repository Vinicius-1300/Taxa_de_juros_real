import requests
from datetime import datetime, timedelta

data_inicial = (datetime.now() - timedelta(days=365)).strftime("%d/%m/%Y")
data_final = datetime.now().strftime("%d/%m/%Y")
url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}" #API

def inflacao():
    try:
        req = requests.get(url)
        req.raise_for_status() # Função do modulo requests que retorna o status da api
        dados = req.json()
        inflacao_acumulada = sum(float(item["valor"]) for item in dados if "valor" in item)
        return inflacao_acumulada
    except (requests.exceptions.RequestException, ValueError, KeyError):
        print('Erro, dados não encontrados')
        return None
    
#Função responsavel por validar se a informação será valor flutuante 
def validacao_float(info):
    while True:
        try:
            valor = float(input(info))
        except (ValueError, TypeError):
            print('\33[31mERRO, por favor digite um número decimal válido')
            continue
        else:
            return valor