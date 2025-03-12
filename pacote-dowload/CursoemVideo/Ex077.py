palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for p in palavras:
    print(f'\nNa Palavra {p.upper()} temos as Vogais ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')



