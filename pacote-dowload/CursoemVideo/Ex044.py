''' print('-=-' * 3, 'Loja do André', '-=-' * 3) '''
'''print('{:=^40}'.format(' Loja do André '))'''
print(f'{" JUNIORS PAY ":=^40}')
preco = float(input('Valor da Compra: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Opção -> '))
if opcao == 1:
    desc = preco * (10/100)
    valor = preco - desc
    print(f'''    Forma de Pagamento: à vista dinherio/cheque
    Preço Normal: R${preco:.2f}
    Desconto: R${desc:.2f}
    Preço com Desconto: R${valor:.2f}''')
elif opcao == 2:
    desc = preco * (5/100)
    valor = preco - desc
    print(f'''    Forma de Pagamento: à vista no cartão
    Preço Normal: R${preco:.2f}
    Desconto: R${desc:.2f}
    Preço com Desconto: R${valor:.2f}''')
elif opcao == 3:
    parcela = preco / 2
    desc = preco * 0
    valor = preco - 0
    print(f'''    Forma de Pagamento: 2x vezes no cartão
    Preço Normal: R${preco:.2f}
    Desconto: R${desc:.2f}
    Preço com Desconto: R${valor:.2f}
    Valor da Parcela: R${parcela:.2f}''')
elif opcao == 4:
    parcela = int(input('Parcelas: '))
    juros = preco * (20/100)
    valor = preco + juros
    valorParcela = valor / parcela
    print(f'''    Forma de Pagamento: {parcela}x no cartão
    Preço Normal: R${preco:.2f}
    Juros: R${juros:.2f}
    Preço com Juros: R${valor:.2f}
    Valor da Parcela: R${valorParcela:.2f}''')
else:
    print(' OPÇÃO INVÁLIDA! \n TENTE NOVAMENTE!')
