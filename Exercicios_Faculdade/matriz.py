#Considere a matriz quadrada de inteiros, onde a quantidade de linhas e colunas 
#informadas pelo usuário 
#Calcule a soma dos elementos da diagonal principal da matriz

n = int(input("Digite o tamanho da matriz "))
contador1 = 0
contador2 = 0

while contador1 < n:
    print()
    contador1 += 1
    while contador2 < n:
        print(contador1, contador2)
        contador2 += 1