print('--' * 20)
print(f'{"Loja do Mestre André":^40}')
print('--' * 20)
ValorCompra = ProdutoMil = ProdutoBarato = contador = 0
NomeProdutoBarato = ' '
while True:
    produto = str(input('Produto: ')).strip().upper()
    valor = float(input('Preço: R$'))
    ValorCompra += valor
    contador += 1
    if contador == 1 or valor < ProdutoBarato:
        ProdutoBarato = valor
        NomeProdutoBarato = produto
    if valor > 1000.00:
        ProdutoMil += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer Continua? [S/N] \n-> ')).upper().split()[0]
    if resposta in 'N':
        break
print(f'{" FIM DA COMPRA ":-^40}')
print(f'Total da Compra: R${ValorCompra:.2f}')
print(f'Produto Custando Mais de R$1000,00: {ProdutoMil}')
print(f'Produto Mais Barato foi {NomeProdutoBarato}: R${ProdutoBarato:.2f}')
