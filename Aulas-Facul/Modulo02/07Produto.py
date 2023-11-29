class  Produto:
    def __init__(self):
        self.nome = ""
        self.sobreNome = ""
        self.idade = ""
        self.altura = ""
 
 
# e necessario colocar valores vazio, campos faltando e so colocar o nome = '' ai ele aceita valores vazio
class  Produtos:
    def __init__(self, nome = '', sobreNome = '', idade = '', altura = ''):
        self.nome = nome
        self.sobreNome = sobreNome
        self.idade = idade
        self.altura = altura
    
       
produto0 = Produto()
produto0.nome = "Manoel"
produto0.idade = "18"

produto1 = Produtos('Bratriz','Quens', 18, 1.60)



print(produto0.__dict__)
print(produto1.__dict__)