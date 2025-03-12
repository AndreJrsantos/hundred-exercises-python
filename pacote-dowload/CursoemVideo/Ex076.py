lista_preco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
               'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
               'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-~-' * 18)
print(f'{" LISTAGEM DE PREÇOS ":^40}')
print('-~-' * 18)

for posicao in range(0, len(lista_preco)):
    if posicao % 2 == 0:
        print(f'{lista_preco[posicao]:.<40}', end='')
    else:
        print(f'R$ {lista_preco[posicao]:>6.2f}')

print('-~-' * 18)
