#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como 
#parâmetro e devolve o maior número primo menor ou igual ao número passado à função


def maior_primo(n):
    while n >= 2:
        divisor = 1
        cont = 0

        while divisor <= n:
            if n % divisor == 0:
                cont += 1
            divisor += 1

        if cont == 2:
            return n
        n -= 1



print(maior_primo(100))
print(maior_primo(7))