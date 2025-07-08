"""Crie uma classe Funcionario que herda da classe Pessoa.
Ela deve ter um novo atributo salario e um método mostrar_salario que imprime o salário da pessoa.

"""

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

class Funcionario(Pessoa):
    
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self._salario = salario
        
    def get_salario(self):
        return self._salario
    
    def mostrar_salario(self):
        print(f"Salário: R${self._salario}")
    
f1 = Funcionario("Fernando", 33, 1500)
f1.mostrar_salario()