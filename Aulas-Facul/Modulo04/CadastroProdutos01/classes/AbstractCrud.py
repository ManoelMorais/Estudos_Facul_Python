import json
from abc import ABC

class AbstractCrud(ABC):
    
    
    def Detalhar(self):
        return self.__dict__
    
    def __GravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)
         
        print('Operação realizada com sucesso')
    
    
    @classmethod  
    def Consultar(cls, item = None):
        try:
            with open(cls.arquivo) as file:       
                lista = json.load(file)
                
            return lista[item] if isinstance(item, int) else lista
            
        except Exception:
            return []
    

    def Inserir(self):
        
        lista = self.Consultar()
        lista.append(self.Detalhar())
        self.__GravarArquivo()
        
    def Alterar(self, item):
        
        lista = self.Consultar()
        lista[item] = self.Detalhar()
        self.__GravarArquivo()
        
    @classmethod    
    def Listartodos(cls):
        
        lista = cls.Consultar()
        for i, p in enumerate(lista):
            print(f"{i} - {p}")
            
    @classmethod     
    def Excluir(cls, item):
        lista = cls.Consultar()
        del lista[item]
        
        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)
         
        print('Operação excluido com sucesso')
    