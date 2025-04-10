n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n2 > n1:
    if n3 > n2:
        print('crescente')
    else:
        print('não está em ordem crescente')
else:
    print('não está em ordem crescente ')