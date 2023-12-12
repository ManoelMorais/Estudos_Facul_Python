from classes.AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):
    
    arquivo = 'db/categoria.json'
    
    def __init__(self, nome):
        self.nome = nome
        