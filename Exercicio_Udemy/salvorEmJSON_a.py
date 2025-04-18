# Exercício - Salve sua classe em JSON
 # Salve os dados da sua classe em JSON
 # e depois crie novamente as instâncias
 # da classe com os dados salvos
 # Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade, naturalidade):
        self.nome = nome
        self.idade = idade
        self.naturalidade = naturalidade

p1 = Pessoa('Silas', 20, 'Brasileiro')
p2= Pessoa('João', 30, 'Brasileiro')
p3 = Pessoa('Maria', 20, 'Francesa')

pessoas = [vars(p1), vars(p2), vars(p3)]
#pessoa_dict = vars(p1)

with open('pessoa.json', 'w', encoding='utf8') as f:
    json.dump(pessoas, f, ensure_ascii=False, indent=2)