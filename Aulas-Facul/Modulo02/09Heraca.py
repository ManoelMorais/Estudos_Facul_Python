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
    
# Imovel = Imovel('Solar do Cerrado', 'df', 500000)
# Imovel.endereco = 'ABC'
# Imovel.area = '2000'
# Imovel.detalhar()
    
class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        super().__init__(nome, uf, valor, endereco = '', area = '')
        self.quartos = 0
        self.banheiros = 0
        self.piscina = False
    
class ImovelComercial(Imovel):
    ...    

casa = ImovelResidencial('Mica casa', 'se', 290000, 'na pqp')
casa.detalhar()


clinica = ImovelComercial('Clinica', 'sp', 400000)
clinica.detalhar()
