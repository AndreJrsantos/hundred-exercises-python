from time import sleep
from math import factorial
print(f'{" Calculadora de Fatorial! " :~^40}')
n = int(input('Informe o Número a ser Calculado: '))
print(f'Calculando {n}!...')
sleep(1.5)
# print(f'O Fatorial de {n}! é {factorial(n)}.')

fatorial = 1
f = 1
c = n
i = n
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)
print()
print('Com FOR')
for i in range(i, 0, -1):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
print(f)