n = int(input('Digite um valor: '))
resultado3 = n 
quantidade_impares = n
while quantidade_impares < n:

    if n == 0:
        print('1')
    else:
        while n != 1:
            n = n - 1
            resultado3 *= n
            quantidade_impares += 1
        print(resultado3)