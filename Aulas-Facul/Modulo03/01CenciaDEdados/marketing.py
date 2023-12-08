import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimento, cliques, conversoes):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversoes = conversoes
        
    def cpc(self):
        return self.investimento / self.cliques
    
campanhas = [
    Campanha("Facebook", 1000, 10000, 100000),
    Campanha("Instagram", 2000, 20000, 200000),
    Campanha("Twitter", 3000, 30000, 300000),
    Campanha("Youtube", 4000, 40000, 400000)
]

canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]        

plt.bar(canais, cpcs)
plt.title("Custos por Click")
plt.xlabel("Canal")
plt.ylabel("Custo em R$")
plt.show()

