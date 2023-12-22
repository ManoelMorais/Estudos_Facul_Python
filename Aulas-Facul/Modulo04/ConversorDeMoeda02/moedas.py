import requests

def get_cotacao():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data['rates']
    else:
        print('Error ao obter cotação', response.status_code)
        return None
        
def converterCotacao(origem = 'USD', destino = 'BRL', valor = 1):
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 4)

