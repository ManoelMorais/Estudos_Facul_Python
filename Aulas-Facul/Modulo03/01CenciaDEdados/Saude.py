import numpy as np
import pandas as pd


class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade  
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

paciente = {
    "Paciente 1": Paciente("Maria", 25, "F", 60, 1.60),
    "Paciente 2": Paciente("João", 30, "M", 70, 1.70),
    "Paciente 3": Paciente("Pedro", 35, "M", 80, 1.80),
    "Paciente 4": Paciente("Ana", 40, "F", 90, 1.90)
}


l_pacientes = [p.__dict__ for p in paciente.values()]


df_pacientes = pd.DataFrame.from_records(l_pacientes, index=paciente.keys())

df_pacientes["IMC"] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)

media = np.mean(df_pacientes["IMC"])

sobrepeso = df_pacientes[df_pacientes["IMC"] > 25]

percentual = len(sobrepeso) / len(df_pacientes) * 100

print(percentual)

        