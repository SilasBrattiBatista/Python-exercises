#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math

n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {math.trunc(n)}')