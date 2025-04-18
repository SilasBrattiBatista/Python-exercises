'''Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, 
retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.'''

n = int(input('Digite a quantidade de peças no tabuleiro: '))
m = int(input('Digite a quantidade máxima de peças que podem ser retiradas: '))

x = (m + 1)

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
            jogadaInvalida = False

    print(f'Você tirou {pecasTiradas} peças')
    n -= pecasTiradas
    return n


print(usuario_escolhe_jogada(n, m))
print(n)

#def computador_escolhe_jogada(n, m): 
