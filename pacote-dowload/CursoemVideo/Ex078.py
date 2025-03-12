lista = list()
maior = list()
menor = list()
for cont in range(0, 5):
    lista.append(int(input(f'Digite o Valor para a Posição {cont}: ')))
for c, cont in enumerate(lista):
    if cont == max(lista):
        maior.append(c)
    if cont == min(lista):
        menor.append(c)
print(f'Lista Completa: {lista}')
print(f'O Maior Valor Digitado foi {max(lista)} na Posição {maior}')
print(f'O Menor Valor Digitado foi {min(lista)} na Posição {menor}')
