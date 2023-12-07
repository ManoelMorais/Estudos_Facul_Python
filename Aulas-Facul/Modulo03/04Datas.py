from datetime import datetime

#       MODO 01

# def formatarData():
#     Data = datetime(2023, 12, 7)
#     return datetime.strftime(Data, '%Y/%d/%m')

# # %d => Dia
# # %Y => Ano completo com as 4 casas decimais
# # %y => Ano so com as duas ultimas casas decimais
# # %m => mês

# print(formatarData())



#       MODO 02

# def formatarData(Data):
#     return datetime.strftime(Data, '%Y/%d/%m')

# Data = datetime.now()
# print(formatarData(Data))



#       MODO 03

# def formatarData(Data = datetime.now()):
#     return datetime.strftime(Data, '%Y/%d/%m')

# Data = datetime.now(2023, 12, 07)
# print(formatarData(Data))


#       MODO 04

# def formatarData(Data = datetime.now()):
#     return datetime.strftime(Data, '%Y/%d/%m')

# print(formatarData())


#       MODO 05

def formatarData(Data = datetime.now(), formato = '%d/%m/%Y'):
    return datetime.strftime(Data, formato)

# print(formatarData())


#       MODO 06

# def criarData( data, formato = '%Y-%m-%d'):
#     return datetime.strftime(data, formato)



