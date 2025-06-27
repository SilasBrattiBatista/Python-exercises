#imprimindo os retângulos sem preenchimento, de forma que os caracteres que não 
#estiverem na borda do retângulo sejam espaços.

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
contadorAltura = 0

while contadorAltura < altura:
    contadorLargura = 0
    
    
    while contadorLargura < largura:
        if (contadorAltura == 0 or contadorAltura == (altura - 1)) or (contadorLargura == 0 or contadorLargura == (largura - 1)):
            print("#", end="") 
        else:
            print(" ", end="")
            
        contadorLargura += 1
        
    contadorAltura += 1
    print()