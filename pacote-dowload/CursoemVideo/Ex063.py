print(f'~~' * 20)
print(f'{"Sequência Fibonacci" :^40}')
print(f'~~' * 20)
termos = int(input('Informe a Quantidade de Termos das Sequência: '))
a = 0
b = 1
c = 0
cont = 1
if termos == 1:
    print(a, end=' -> ')
elif termos == 2:
    print(f'{a} -> {b}', end=' -> ')
else:
    print(f'{a} -> {b}', end=' -> ')
    while cont <= (termos - 2):
        c = a + b
        print(c, end=' -> ')
        a = b
        b = c
        cont += 1
print('FIM!')
