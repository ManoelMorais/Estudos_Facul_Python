from abc import ABC, abstractclassmethod


class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self.valor = valor
        self.area = area
        self.uf = uf
        self.endereco = endereco
        
        #opcional, não recomendado
    # def getNome(self):
    #     return self.nome
    
    # def setNome(self, nome):
    #     self.nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    def detalhar(self):
        print(self.__dict__)
        

class ImovelComercial(Imovel):
    ...    

clinica = ImovelComercial('Clinica', 'sp', 400000)
clinica.nome = 'Clinica São Carlos'
print(clinica.nome)
clinica.detalhar()
