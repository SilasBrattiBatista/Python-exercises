# Exercício - Lista de tarefas com desfazer e refazer
 # Música para codar =)
 # Everybody wants to rule the world - Tears for fears
 # todo = [] -> lista de tarefas
 # todo = ['fazer café'] -> Adicionar fazer café
 # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
 # desfazer = ['fazer café',] -> Refazer ['caminhar']
 # desfazer = [] -> Refazer ['caminhar', 'fazer café']
 # refazer = todo ['fazer café']
 # refazer = todo ['fazer café', 'caminhar']
import os


lista_Tarefas = []
lista_Refazer = []
sair = False

while sair != True:

    print('Comandos: listar, desfazer, refazer')
    operacao = str(input('Digite uma tarefa ou um comando: ')).lower()
    print('')

    if operacao == 'listar':
        print('TAREFAS:')
        for item in lista_Tarefas:
            print(item)
        print('')

    elif operacao == 'sair':
        for item in lista_Tarefas:
            print(item)
        sair = True

    elif operacao == 'desfazer':

        if len(lista_Tarefas) == 0:
            print('Nada a desfazer!')
        else:
            adicionar_Lista_Refazer = lista_Tarefas[-1]
            lista_Refazer.append(adicionar_Lista_Refazer)
            lista_Tarefas.pop()

    elif operacao == 'refazer':

        if len(lista_Refazer) == 0:
            print('Nada a refazer!')
        else:
            adicionar_Lista_Tarefas = lista_Refazer[-1]
            lista_Tarefas.append(adicionar_Lista_Tarefas)
            lista_Refazer.pop()

    elif operacao == 'clear':
        os.system('cls')

    else:
        lista_Tarefas.append(operacao)