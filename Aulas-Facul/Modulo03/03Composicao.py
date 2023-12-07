# import 04Datas
# a importação não esta funcionando

class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo
        
        
    def taxaAgua(self, consumo):
        
        # print("Data de leitura:", 04Datas.formatarData())
        
        match self.tipo:
            case 'Clinica': return consumo * 1.5
            case 'Casa': return consumo * 1
            case 'Hotel': return consumo * 2.5
            case _: return consumo * 0.5

class Imovel:
    
    imposto = 0.2
    
    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        
    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def __str__(self):
        return str(self.__dict__)
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatico():
        print('Metodo estatico')
        
    @classmethod    
    def metodoClass(cls):
        print('chamou o metodo de imposto', cls.imposto)
        
        
imovel1 = Imovel('Casa', 2, 2)
mansao = Imovel('Mansão', 4, 5)


categoria = Categoria('Hotel')
hotel = Imovel('Hotel do chico', 134, 34)
hotel.categoria = categoria
print(hotel.categoria.taxaAgua(300))

# print(imovel1.somarAposentos())
# print(mansao.somarAposentos())

# imovel1.metodoEstatico()
# Imovel.metodoEstatico()
# imovel1.metodoClass()





