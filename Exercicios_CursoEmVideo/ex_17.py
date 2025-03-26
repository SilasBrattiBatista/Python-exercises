#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')