#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = (altura * largura)
quantidadeParaPintarParede = (area / 2)

print(f'Sua parede tem uma dimensão de {largura}x{altura} e a sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará  de {quantidadeParaPintarParede}l')