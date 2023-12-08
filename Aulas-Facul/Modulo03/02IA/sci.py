from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso
        
produto = {
    Produto("Produto 1", 60.50, 0.70),
    Produto("Produto 2", 50.50, 0.80),
    Produto("Produto 3", 40.50, 0.90),
    Produto("Produto 4", 30.50, 1.00),
    Produto("Produto 5", 20.50, 1.10),
    Produto("Produto 6", 10.50, 1.20),
}

preco = [[p.preco, p.peso] for p in produto]
matriz = np.array(preco)

kmeans = KMeans(n_init='auto', n_clusters=2, random_state=0).fit(matriz)
labels = kmeans.labels_

for i in range(4):
    print(f"Grupo {i + 1}:")
    for j in range(len(produto)):
        if labels[j] == i:
            print(" - ", produto[j].nome)
