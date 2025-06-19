#Considere a matriz quadrada de inteiros, onde a quantidade de linhas e colunas 
#informadas pelo usuário 
#Calcule a soma dos elementos da diagonal principal da matriz

n = int(input("Digite o tamanho da matriz"))
matriz = ""

for i in range(n):
    for j in range(n):
        print(i, j)