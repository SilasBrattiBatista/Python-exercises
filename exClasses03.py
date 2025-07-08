"""Adapte a classe Pessoa para que:

Os atributos sejam protegidos (use _nome e _idade);

Tenha métodos mudar_nome e mudar_idade que alteram os valores com verificação;

mudar_idade deve impedir idades negativas."""

class Pessoa:
    
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
    def mudar_nome(self, novoNome):
        self._nome = novoNome
    
    def mudar_idade(self, novaIdade):
        
        if novaIdade < 1:
            print("Idade Inválida")
        else:
            self._idade = novaIdade
            
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade
        
            
p1 = Pessoa("Silas", 20)

p1.mudar_idade(0)
p1.mudar_nome("Silas Bratti Batista")
p1.mudar_idade(21)

print(p1.get_nome())
print(p1.get_idade())