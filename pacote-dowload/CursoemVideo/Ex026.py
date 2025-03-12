text = str(input('Digite uma Frase: ')).strip().upper()
print('A Letra "a" aparece {} Vezes!'.format(text.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(text.find('A') + 1))
print('A letra "a" aparece pela última vez na posição {}.'.format(text.rfind('A') + 1))
