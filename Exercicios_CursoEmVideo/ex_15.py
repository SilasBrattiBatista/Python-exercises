#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugado = int(input('Quantos dias alugados? '))
kmRodado = float(input('Quantos Km rodado ? '))

totalPagar = (diasAlugado * 60) + (kmRodado * 0.15)

print(f'O total a pagar é de R${totalPagar}')