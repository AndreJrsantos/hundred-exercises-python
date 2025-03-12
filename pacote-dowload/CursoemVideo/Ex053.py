frase = str(input('Digite sua Palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]'''
inverso = junto[::-1]
print(f'O inverso é: {inverso}')
if inverso == junto:
    print(f'A frase "{frase}" É um PALÍNDROMO!')
else:
    print(f'A frase "{frase}" Não é um PALÍNDROMO!')

