print('Soma Entre todos os Numeros Impares multiplos de 3 1-500')
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
print(f'A soma é {s}')
