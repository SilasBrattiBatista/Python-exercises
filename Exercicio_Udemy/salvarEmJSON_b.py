# Exercício - Salve sua classe em JSON
 # Salve os dados da sua classe em JSON
 # e depois crie novamente as instâncias
 # da classe com os dados salvos
 # Faça em arquivos separados.
import json
from salvorEmJSON_a import Pessoa

with open('pessoa.json', 'r', encoding='utf8') as f:
    dados = json.load(f)
    print(dados)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3= Pessoa(**dados[2])



print(p1.nome)
print(p2.nome)
print(p3.nome)