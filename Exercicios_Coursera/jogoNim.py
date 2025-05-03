'''Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, 
retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.'''
def usuario_escolhe_jogada(n, m):

    while True:
        pecasATirar = int(input('Quantas peças você vai tirar? '))
        print()

        if pecasATirar > n or pecasATirar > m:
            print('Oops! Jogada inválida! Tente de novo')
            print()
        else:   
            pecasTiradas = pecasATirar
            return pecasTiradas



def computador_escolhe_jogada(n, m):

    x = (m + 1)

    while True:
            
        if ((n - x) % x) == 0:
            return x
        elif (n - x) == 0:
            return x
        
        x -= 1


def jogo():

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    x = (m + 1)
    contador = 0

    if (n % x) == 0:
        print('Você começa!\n')
        pecasTiradas = usuario_escolhe_jogada(n, m)
        print(f'Você tirou {pecasTiradas} peças')
        contador += 1
        n -= pecasTiradas
        print(f'Agora restam {n} peças no tabuleiro')
        print()
    else:
        print('Computador começa!\n')
        pecasTiradas = computador_escolhe_jogada(n, m)
        print(f'O computador tirou {pecasTiradas} peças')
        n -= pecasTiradas
        print(f'Agora restam {n} peças no tabuleiro')
        print()

    while n != 0:

            contador += 1

            if (contador % 2) == 0:
                pecasTiradas = computador_escolhe_jogada(n, m)
                print(f'O computador tirou {pecasTiradas} peças')
                n -= pecasTiradas
                print(f'Agora restam {n} peças no tabuleiro')
                print()
            else:
                pecasTiradas = usuario_escolhe_jogada(n, m)
                print(f'Você tirou {pecasTiradas} peças')
                n -= pecasTiradas
                print(f'Agora restam {n} peças no tabuleiro')
                print()
    print('Fim do Jogo! O computador ganhou!')
    print()
            
        



def partida():


    print('Bem-vindo ao jogo do NIM! Escolha: ')

    tipoPartida = int(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato '))
    
    if tipoPartida == 1:
        jogo()
    elif tipoPartida == 2:
        print()
        print('Você escolheu um campeonato!')
        print()
        
        contador = 1
        while contador < 3:
            print(f'**** Rodada {contador} ****')
            print()
            jogo()
            contador += 1


#def computador_escolhe_jogada(n, m): 
partida()