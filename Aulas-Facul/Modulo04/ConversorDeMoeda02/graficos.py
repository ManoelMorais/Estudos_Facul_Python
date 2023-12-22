import matplotlib.pyplot as plt
from moedas import get_cotacao

cotacoes = get_cotacao()

l_moedas = [ "USD - Dólar", "EUR - Euro", "YER - Libras"]
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]

def G_Barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões para real')
    plt.xlabel('Moedas')
    plt.ylabel('BRL')
    plt.show()
    
def G_Pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Conversões para real')
    plt.show()
 