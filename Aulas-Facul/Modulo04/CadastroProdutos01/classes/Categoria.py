from classes.AbstractCrud import AbstractCrud

class Categoria(AbstractCrud):
    def __init__(self, nome):
        self.nome = nome
        