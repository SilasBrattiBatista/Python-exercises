#Escreva a função vogal que recebe um único caractere como parâmetro e 
# devolve True se ele for uma vogal e False se for uma consoante.

def vogal(letra):

    if letra in 'aeiouAEIOU':
        return True
    else:
        return False
    
print(vogal('b'))
print(vogal('A'))