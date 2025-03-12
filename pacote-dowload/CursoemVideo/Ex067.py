cont = 0
while True:
    tabuada = int(input(f'Tabuada de qual Número: '))
    print('~' * 30)
    if tabuada < 0:
        break
    else:
        for cont in range(1, 11):
            print(f'{tabuada} x {cont}  = {tabuada * cont} ')
    print('~' * 30)
print('Encerrado!')
