"""Crie uma classe Produto com os atributos:

nome

preco

E um método aplicar_desconto(percentual) que reduz o preço pelo percentual informado."""

class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def percentual(self, percentual):
        self.preco = self.preco + ((percentual / 100) * self.preco)
        print(self.preco)
    
p1 = Produto("Banana", 10)

p1.percentual(50)
