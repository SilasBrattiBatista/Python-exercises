#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos 
#Faça um programa que leia o nome dos quatro alunos e mostre a order sorteada

from random import shuffle

al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentasão será')
print(lista)