produto = str(input('Digite o nome do produto: '))
quantidadeMaxima = float(input('Digite a quantidae Máxima que o estoque pode conter: '))
quantidadeMinima = float(input('Digite a quantidade Minima que o estoque pode conter: '))
estoque = float(input('Digite a quantidade do estoque: '))


if estoque < quantidadeMinima or estoque > quantidadeMaxima:
    print('Digite uma quantidade de estoque valida!')
elif quantidadeMaxima < quantidadeMinima:
    print('A quantidade máxima é menor que a quantidade mínima, digite uma quantidade valida')
elif quantidadeMinima > quantidadeMaxima:
    print('A quantidade minima é maior que a quantidade maxima, digite uma quantidade valida')
else:
    operacao = int(input('Digite a operação desejada \n 1 - Adicionar ao estoque \n 2 - retirar do estoque\n'))
    
    if operacao == 1:
        adicaoAoEstoque = float(input('Digite a quantidade que você deseja adicionar ao estoque? '))

        if (adicaoAoEstoque + estoque) > quantidadeMaxima:
            print('Ao adicionar essa quantidade ao estoque ele ultrapassará a quantidade máxima permitida.')
            print('Estoque atual', estoque)
        else:
            print('Quantidade adicionada ao estoque.')
            print('Estoque atual ', estoque + adicaoAoEstoque)

    elif operacao == 2:
        subtracaoAoEstoque = float(input('Digite a quantidade que você deseja retirar do estoque? '))
        quantidadeAtual = estoque - subtracaoAoEstoque

        if quantidadeAtual < quantidadeMinima:
            print('Ao retirar essa quantidade ao estoque ele ultrapassará a quantidade mínima permitida.')
            print('Quantidade atual', estoque)
        else:
            print('Quantidade retirada do estoque.')
            print('Estoque atual ', estoque - subtracaoAoEstoque)

    else:
        print('Operação Inválida!')
        