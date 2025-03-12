
n1 = int(input('Digite um Número: '))
n2 = int(input('Digite um Número: '))
n3 = int(input('Digite um Número: '))
n4 = int(input('Digite um Número: '))
n5 = int(input('Digite um Número: '))
tupla = (n1, n2, n3, n4, n5)
print(f'Você digitou: {tupla}')
print(f'A Número 9 aparece {tupla.count(9)}')
if 3 in tupla:
    print(f'O Número 3 aparece na Posição {tupla.index(3) + 1}')
else:
    print('Número 3 não foi digitado')
print(f'Os Números Pares foram: ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' -> ')
print('FIM!')
