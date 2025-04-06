#Escreva um programa que mostre na tela um menu de pratos (pelo menos 5),
#cada um associado a um número. Por exemplo:
#   1 - Miojo
#   2 – Ensopado
#Quando um número é selecionado, o programa deve exibir uma breve
#descrição do prato.
#Por exemplo, ao digitar 1, o programa mostra: “Macarrão instantâneo”.

p1 = 'Bife a cavalo'
p2 = 'Bife a parmegiana'
p3 = 'Nhoque'
p4 = 'Macarrão ao molho Branco'
p5 = 'Macarrão com Carne Moida'

print(f'Menu: \n 1 - {p1} \n 2 - {p2} \n 3 - {p3} \n 4 - {p4} \n 5 - {p5}')

pedido = int(input('Digite o número do prato escolhido'))

if pedido == 1:
    print('Bife com ovo frito em cima')
elif pedido == 2:
    print('Bife empanado com molho e queijo')
elif pedido == 3:
    print('Massa de batata em bolinhos')
elif pedido == 4:
    print('Macarrão com molho cremoso e branco')
elif pedido == 5:
    print('Macarrão com molho de carne moída')
else:
    print('Você não digitou uma opção válida')