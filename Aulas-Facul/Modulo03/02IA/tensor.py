import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'


class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco  
        self.categoria = categoria
        
produtos = [
    Produto("camisa", 20.99, "Roupa"),
    Produto("regata", 10.99, "Roupa"),
    Produto("shot", 15.89, "Roupa"),
    Produto("celular", 399.99, "tecnologia"),
    Produto("livro", 59.99, "Objeto"),
    Produto("notebook", 699.99, "tecnologia"),
    Produto("brinquedo", 30.99, "Objeto"),
]

nomes = tf.constant([p.nome for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])
precos = tf.constant([p.preco for p in produtos])

media = tf.reduce_mean(precos)
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, 'tecnologia'))

print(media)
print(eletronicos)
