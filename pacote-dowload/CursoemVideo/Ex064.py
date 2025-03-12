'''print(f'{" Calculadora de Soma " :~^40}')
n = int(input('OBS: digite 999 para Visualizar o Resultado! \nDigite um Número para Ser Somado: '))
soma = n
while n != 999:
    n = int(input('OBS: digite 999 para Visualizar o Resultado! \nDigite outro Número para Ser Somado: '))
    soma += n
soma -= 999
print(f'A Soma dos Números Digitados é: {soma}')'''

print(f'{" Calculadora de Soma " :~^40}')
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um Número [999 para Parar!]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Você digitou {cont} números!')
print(f'A Soma é {soma}!')
