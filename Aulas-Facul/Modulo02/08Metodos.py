class  Produtos:
    def __init__(self, nome = '', valor = '', quantidade = 0, marca = '', modelo = ''):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.marca = marca
        self.modelo = modelo
        
    def vender(self, quantidade):
        if(quantidade > self.quantidade):
            print("****************************")
            print("Não há mais no estoque esse produto")
            print("Quantidade", self.quantidade)
            print("****************************")
        else:
            #self.quantidade = self.quantidade - quantidade
            self.quantidade -= quantidade
    
    def comprar(self, quantidade):
        #self.quantidade = self.quantidade + quantidade
        self.quantidade += quantidade
    
    
produto1 = Produtos('Celular', 4300, 78, "Iphone", "Iphone 12")
produto1.comprar(10)
produto1.vender(100)

print(produto1.__dict__)
