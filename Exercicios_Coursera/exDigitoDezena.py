numero = int(input('Digite um número inteiro: '))

dezena = numero // 10
ultimo_digito = str(dezena)
digito_dezena = ultimo_digito[-1]


print(f'O digito das dezenas é {digito_dezena}')