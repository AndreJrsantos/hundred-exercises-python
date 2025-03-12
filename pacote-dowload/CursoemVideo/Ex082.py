lista = []
pares = []
impares = []
while True:
    n = int(input('Informe um Número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Quer continuar? [S/N] \n-> ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

listaa = []
listap = []
listai = []
while True:
    listaa.append(int(input('Didite um valor: ')))
    sn = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if sn == 'N':
        break
for pos, valor in enumerate(listaa):
    if valor % 2 == 0:
        listap.append(valor)
    else:
        listai.append(valor)
print('=°=' * 14)
print(f'A lista completa é: {listaa}')
print(f'A lista dos valores PARES é: {listap}')
print(f'A lista dos valores ÍMPARES é: {listai}')
