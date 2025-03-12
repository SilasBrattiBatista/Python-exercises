#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o valor do produto: '))
precoComDesc = (preco - ((preco * 5) / 100))

print(f'O produto que custava {preco}, com 5% de desconto ficará {precoComDesc}')