#Dada uma letra, mostre se essa letra é ou não uma vogal (pode considerar
# apenas letras minúsculas)
letra = str(input('Digite uma letra para saber se ela é vogal ou não: '))
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print('Essa é letra é uma vogal')
else:
    print('Essa letra é uma consoante')