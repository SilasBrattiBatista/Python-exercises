#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

n = float(input('Digite um número em metros para saber seu valor em centimetros e milimetros '))

centimetros = n * 100
milimetros = n * 1000

print(f'O valor {n}, em centimetros {centimetros} e milimetro {milimetros}')
