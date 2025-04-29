'''Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, 
retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.'''
def usuario_escolhe_jogada(n, m):
    jogadaInvalida = True 

    while jogadaInvalida:
        pecasATirar = int(input('Quantas peças você vai tirar? '))

        if pecasATirar > n:
            print('Oops! Jogada inválida! Tente de novo')
        elif pecasATirar > m:
            print('Oops! Jogada inválida! Tente de novo')
        else:   
            pecasTiradas = pecasATirar   

    print(f'Você tirou {pecasTiradas} peças')
    n -= pecasTiradas
    return n


def computador_escolhe_jogada(n, m):

    x = (m + 1)

    while True:
            
        if ((n - x) % x) == 0:
            return n - x
        elif (n - x) == 0:
            return n - x
        
        x -= 1
            

def partida():
    n = int(input('Digite a quantidade de peças no tabuleiro: '))
    m = int(input('Digite a quantidade máxima de peças que podem ser retiradas: '))
    x = (m + 1)
    quemComeca = "Ninguem"
    contador = 0

    if (n % x) == 0:
        print('Você começa!')
        n = usuario_escolhe_jogada(n, m)
        quemComeca = 'usuario'
    else:
        print('Computador começa!')
        n = computador_escolhe_jogada(n, m)
        quemComeca = 'computador'

    while m != 0:

        if quemComeca == 'usuario':
            n  = computador_escolhe_jogada(n, m)
            quemComeca = 'nada'
            contador += 0
        elif quemComeca == 'computador':
            n = usuario_escolhe_jogada(n, m)
            quemComeca = 'nada'
            contador += 1
        else:
            contador += 1

            if (contador % 2) == 0:
                n = computador_escolhe_jogada(n, m)
            else:
                n = computador_escolhe_jogada(n, m)

        



#def computador_escolhe_jogada(n, m): 
