from abc import ABC, abstractclassmethod


class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self._valor = valor
        self._area = area
        self._uf = uf
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    def calcimposto(self):
        return self._valor * 0.02
    
    def detalhar(self):
        print(self.__dict__)
        

class ImovelComercial(Imovel):
    def calcimposto(self):
        match self._uf:
            case 'SP': taxa * 0.04
            case 'MG': taxa * 0.06
            case 'RJ': taxa * 0.08
            case 'MG': taxa * 0.03
            case 'ES': taxa * 0.01
            case 'MG': taxa * 0.05
            case other: taxa = 0.02 
        
        return self._valor * taxa

clinica = ImovelComercial('Clinica', 'sp', 400000)
clinica.nome = 'Clinica São Carlos'
print(clinica.nome)
clinica.detalhar()

