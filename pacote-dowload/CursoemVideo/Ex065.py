lista = []
p1 = 'S'
while p1 in 'Ss':
    num = int(input('Digite um numero : '))
    p1 = input('Quer continuar ? [S/N]').strip().upper()
    lista.append(num)
    if p1 == 'N':
        break
print(f'Você digitou {len(lista)} numeros e a media foi {sum(lista) / len(lista)} \n O maior valor foi {max(lista)} e o menor foi {min(lista)}')
# len => quantidade de elementos na lista
# sum => soma
# .append => adiciona algo na lista
# min e max => menor e maior número da lista

'''n = int(input('Digite um Número: '))
resp = str(input('Quer Continuar? [S / N] \n->')).strip().upper().strip()[0]
contador = 0
maior = menor = soma = n
if resp == 'N':
    print(f'Média = {n} \nSoma = {n} \nMaior = Não houve um Comparativo. Informe mais Números! \nMenor = Não Houve um Comparativo. Informe mais Números!')
else:
    while resp == 'S':
        n = int(input('Digite um Número: '))
        soma += n
        contador += 1
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        resp = str(input('Quer Continuar? [S / N] \n->')).strip().upper()
    media = soma / contador
    print(f'Média = {media} \nSoma = {soma} \nMaior = {maior} \nMenor = {menor}')'''
