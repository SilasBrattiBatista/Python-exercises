#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possiveis sobre ela

v1 = input('Digite algo: ')

print(f'Seu tipo primitivo é: {type(v1)}')
print(f'Só tem espaços ? {v1.isspace}')
print(f'É um número {v1.isnumeric}')
print(f'É alfabético ? {v1.isalpha}')
print(f'Está em maiúsculas ? {v1.isupper}')
print(f'Está em minúsculas ? {v1.islower}')
