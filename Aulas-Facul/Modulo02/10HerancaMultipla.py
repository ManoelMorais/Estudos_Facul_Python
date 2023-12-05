class Imovel:
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self.nome = nome
        self.valor = valor
        self.area = area
        self.uf = uf
        self.endereco = endereco
        
    def detalhar(self):
        print(self.__dict__)
        
    def calcimposto(self):
        return self.valor * 0.02
    
    
class ImovelRural:
    def __init__(self, hectares = '', curral = '', produtividade = ''):
        self.hectares = hectares
        self.curral = curral
        self.produtividade = produtividade
        
    def mesPlantacao(self, mes):
        match mes:
            case 1: print('milho')
            case 2: print('feijão')
            case 3: print('soja')
            case other: print('algodão')
            
            
class Fazenda(Imovel, ImovelRural):
    ...
    
    
    
fazenda = Fazenda('Fazenda Modelo', 'mg', 1500000)    
fazenda.detalhar()      
print(fazenda.calcimposto())     
fazenda.mesPlantacao(2)
            