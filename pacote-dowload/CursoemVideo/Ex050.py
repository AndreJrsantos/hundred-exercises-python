s = 0
for c in range(0, 6):
    n = int(input('Informe um Número: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma é {s}')
