#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como 
#parâmetro e devolve o maior número primo menor ou igual ao número passado à função
def maior_primo(n):
    primo = 0

    while primo == 0:

        if (n % 2) == 0 or (n % 3) == 0:
            n -= 1
        elif (n > 1) and (n % 2) != 0 and (n % 3) != 0:
            primo = n
        else:
            return 'Número digitado inválido'

    return primo

maior_primo(100)
maior_primo(7)