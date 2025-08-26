#Escreva a função n_primos que recebe como argumento um número inteiro maior ou 
#igual a 2 como parâmetro e devolve a quantidade de números primos que existem 
#entre 2 e n (incluindo 2 e, se for o caso, n).

def ePrimo(n):
    
    qtd: int = 0
    contador: int = 2
    while contador <= n:
        if (n % contador) == 0:
            qtd += 1
        
        contador += 1
        
    if not qtd >= 2:
        return True
        
        
        
def n_primos(n) -> None:
    
    contador: int = 2
    qtd_primo: int = 0
    
    while contador <= n:
        if ePrimo(n):
            qtd_primo += 1
            
        contador += 1
        
    print(qtd_primo)

n_primos(2)