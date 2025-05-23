#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas e minusculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome: "))

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minusculas é {nome.lower()}")
print(f"Seu nome ao todo tem {len(nome.replace(" ", ""))}")
print(f"Seu primeiro nome é {nome.split()[0]}")
