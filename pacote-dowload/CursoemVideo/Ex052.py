'''n = int(input('Informe um Número: '))
if n == 2 or n == 3 or n == 5:
    print(f'{n} É PRIMO!')
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
    print(f'{n} É PRIMO!')
elif n == 1:
    print(f'{n} NÃO É PRIMO!')
else:
    print(f'{n} NÃO É PRIMO!')'''
tot = 0
num = int(input('Digite um Número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO Número {num} foi divísivel {tot} vezes!')
if tot == 2:
    print(f'Logo, o Número {num} é Primo!')
else:
    print(f'Logo, o Número {num} Não é Primo!')
