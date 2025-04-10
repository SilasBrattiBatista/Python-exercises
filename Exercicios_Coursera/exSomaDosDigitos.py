n = int(input("Digite um número inteiro:"))
soma = 0

while n > 0:
    soma = (n % 10) + soma
    n = n // 10

if n < 1:
    print(soma)