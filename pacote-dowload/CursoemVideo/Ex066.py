soma = cont = 0
while True:
    n = int(input('Digite um Número [999 para PARAR!]:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A Soma dos {cont} números é {soma}')
