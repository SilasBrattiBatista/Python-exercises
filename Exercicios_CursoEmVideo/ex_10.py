#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar 
#COnsidere US$1,00 = R$3,27

n = float(input('Digite quanto você tem na carteira: R$'))
dolar = (n / 3.27)

print(f'Com R${n}, você consegue comprar US${dolar} ')