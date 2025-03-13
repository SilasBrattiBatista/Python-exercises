#Crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o seu salário: '))
novo_salario = salario + ((salario * 15) / 100)

print(f'O salário {salario} com um aumento de 15% fica {novo_salario}')