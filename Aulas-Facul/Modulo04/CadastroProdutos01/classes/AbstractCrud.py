import json

class AbstractCrud:
    
    def Detalhar(self):
        return self.__dict__
    
    def Inserir(self):
        
        lista = self.Consultar()
        
        lista.append(self.Detalhar())
        
        with open('db/produtos.json', 'w') as file:
            json.dump(lista, file, indent=4)
        
        print('Registro concluido com sucesso')
        
    def Listartodos(self):
        
        lista = self.Consultar()
        
        for i, p in enumerate(lista):
            print(f"{i} - {p}")
        
    def Consultar(self):
        try:
            with open('db/produtos.json') as file:       
                return json.load(file)
        except Exception:
            return []
        