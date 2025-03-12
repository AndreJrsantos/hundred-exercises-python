lista = []
while True:
    num = (int(input('Digite um Valor: ')))
    if num in lista:
        print('Valor Duplicado! Não Irei adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado!')
    resp = str(input('Quer Continuar? [S/N] \n-> ')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Lista: {lista}')
