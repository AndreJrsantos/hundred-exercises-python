# RESOLUÇÃO GUANABARA #
'''lista = []
for c in range(0, 5):
    n = int(input('Digite um Valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao Final da Lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na Posição {pos} da lista')
                break
            pos += 1
print('-~-' * 14)
print(f'LISTA: {lista}')'''


# RESOLUÇÃO COM SORT #
'''
lista = []
for pos in range(0, 5):
    n = int(input('Digite um Valor: '))
    if n in lista:
    while True:
        print(f"O Número {n} já foi digitado!")
        n = int(input('Digite um Valor: '))
        if n not in lista:
            break
    lista.append(n)
    lista.sort()
    print(f'Valor Adicionado na Posição {lista.index(n)}')
print(f'LISTA: {lista}')
'''
