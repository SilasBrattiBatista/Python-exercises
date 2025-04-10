n = int(input('Digite o valor de n: '))

qntd = 0
contador = 0

while  qntd < n:
    if (contador % 2) != 0:
        print(contador)
        qntd += 1

    contador += 1