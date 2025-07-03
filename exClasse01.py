"""
Crie uma classe chamada Pessoa com os atributos:

nome

idade

Implemente um método apresentar() que imprime algo como:
"Olá, meu nome é João e tenho 30 anos."""

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade}")
        
p1 = Pessoa("Silas", 21)

p1.apresentar()