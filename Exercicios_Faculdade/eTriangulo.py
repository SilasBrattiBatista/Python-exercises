#Escreva um programa que, dado o comprimento de três segmentos de reta,
#determine se eles podem formar um triângulo e, em caso positivo, imprime se o
#triângulo é equilátero, isósceles ou escaleno.
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

eTriangulo = False

if ((reta1 + reta2) > reta3) and ((reta1 + reta3) > reta2) and ((reta2 + reta3) > reta1):
    eTriangulo = True
    print('Considerando as três retas passadas é possível formar um Triangulo')

    if ((reta1 == reta2) != reta3) and ((reta1 == reta3) != reta2) and ((reta2 == reta3) != reta1):
        print('O triangulo é Isósceles')
    elif ((reta1 == reta2) == reta3):
        print('O triangulo é Equilátero')  
    else:
        print('O triangulo é Escaleno')
        
else:
    print('Considerando as três retas passadas não é possível formar um Triangulo')

