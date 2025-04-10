#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como 
#parâmetro e devolve o maior número primo menor ou igual ao número passado à função
def maior_primo(n):
    primo = 0
    divisor = n
    ePrimo = 0

    while primo == 0:

        if (n % divisor) == 0:
            ePrimo += 1
        
        divisor -= 1

maior_primo(100)
maior_primo(7)