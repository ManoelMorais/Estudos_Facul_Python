import pandas as pd

cidade = [
    {"nome": "Aracaju", "uf": "SE", "população": 602.757 },
    {"nome": "Distrito Federal", "uf": "DF", "população": 1602.757 },
    {"nome": "São paulo", "uf": "SP", "população": 6602.757 },
    {"nome": "Rio de Janeiro", "uf": "RJ", "população": 2602.757 },
    {"nome": "Alagoas", "uf": "Al", "população": 802.757 }
]

dataFrame = pd.DataFrame(cidade)

ordernada = dataFrame.sort_values(by="população", ascending=False)

print(ordernada)
print(ordernada.head(2))
print(ordernada.head(2)['nome'])