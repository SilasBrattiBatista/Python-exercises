n = int(input('Digite um número inteiro: '))

contador = 1 
primo = 0

while contador <= n:
    if (n % contador) == 0:
        primo += 1
    
    contador += 1 

if primo == 2:
    print('primo')
else:
    print('não primo')