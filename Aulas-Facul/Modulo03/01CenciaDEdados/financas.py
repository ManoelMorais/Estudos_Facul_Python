import pandas as pd
import matplotlib.pyplot as plt

class Investimentos:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo
        
investimento = {
    "Investimento 1": Investimentos("CDB", 1000, 0.05, 12),
    "Investimento 2": Investimentos("Açôes", 2000, 0.00, 5),
    "Investimento 3": Investimentos("FII", 3000, 0.00, 10),
    "Investimento 4": Investimentos("Tesouro Direto", 4000, 0.05, 7)
}  
        
l_investimentos = [i.__dict__ for i in investimento.values()]

df_investimentos = pd.DataFrame.from_records(l_investimentos, index=investimento.keys())
df_investimentos["Retorno"] = df_investimentos.apply(lambda l: l.valor * ( 1 + l.taxa) ** l.periodo, axis=1)

df_investimentos.plot(kind="bar", x="periodo", y="Retorno", legend="None")
plt.title("Retorno dos Investimentos")
plt.xlabel("Investimento")
plt.ylabel("Retorno")
plt.show()

