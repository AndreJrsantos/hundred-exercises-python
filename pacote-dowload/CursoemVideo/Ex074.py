from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print()
print(f'O Maior Valor Sorteado foi {max(tupla)}')
print(f'O Menor Valor Sorteado foi {min(tupla)}')


from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')