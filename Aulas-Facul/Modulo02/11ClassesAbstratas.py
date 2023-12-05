from abc import ABC, abstractclassmethod

class Imovel(ABC):
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
    
    @abstractclassmethod
    def aluguelSugerido(self):
        ...


class ImovelResidencial(Imovel):
    def aluguelSugerido(self):
        return self.valor * 0.09   
    
class ImovelComercial(Imovel):
    def aluguelSugerido(self):
        return self.valor * 0.16   
    
class ImovelRural(Imovel):
       def aluguelSugerido(self):
        return self.valor * 0.26 
    

casa = ImovelResidencial('Minha casa', 'se', 70000)
casa.detalhar()
print('aluguel sugerido', casa.aluguelSugerido())

clinica = ImovelComercial('Clinica WS', 'sp', 400000)
clinica.detalhar()
print('aluguel sugerido', clinica.aluguelSugerido())

fazenda = ImovelRural('chacara', 'ms', 1200000)
fazenda.detalhar()
print('aluguel sugerido', fazenda.aluguelSugerido())