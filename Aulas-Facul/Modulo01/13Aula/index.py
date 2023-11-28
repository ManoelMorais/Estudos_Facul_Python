import json
import csv

pessoas = [
    {"nome": "Maria", "telefone": "79 99999-9999", "idade": "13"},
    {"nome": "João", "telefone": "79 98888-8888", "idade": "14"},
    {"nome": "Clara", "telefone": "79 97777-7777", "idade": "15"}
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)
    

carros = [
    ["vw", 'virtus', "2019"],
    ["bmw", 'x6', "2023"],
    ["audi", 'q7', "2020"],
]

with open('carros.csv', 'w') as arquivos:
    fileCSV = csv.writer(arquivos)
    fileCSV.writerow(['marca', 'modelo', 'ano'])
    fileCSV.writerow(carros)