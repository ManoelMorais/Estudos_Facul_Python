from abc import ABC, abstractclassmethod


class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self._valor = valor
        self._area = area
        self._uf = uf
        self._endereco = endereco
        #metodo para desprotejer
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

# PUBLICO => pode ser chamado em qualquer lugar
# PROTEJIDO => _ um anderline para o que for protejido 
# PRIVADO => __ dois anderlines para o que for privado
