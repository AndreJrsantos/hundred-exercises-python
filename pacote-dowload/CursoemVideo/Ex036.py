from time import sleep
print('-=-' * 8)
print('\033[32mEMPRÉSTIMO BANCÁRIO!\033[m')
print('-=-' * 8)
valor_casa = float(input('Informe o Valor da sua Casa: R$'))
salario = float(input('Informe o Salário do Comprador: R$'))
tempo = int(input('Quantos Anos de Financiamento? '))
print('Processando Dados...')
print('-=-' * 8)
sleep(1.5)
mensal = valor_casa / (tempo * 12)
if mensal <= (salario * 0.3):
    print(f' Empréstimo Permitido! \n O Valor da Prestação Mensal é R${mensal:.2f}!')
else:
    print(f' Empréstimo Negado! \n O Valor da Prestação Excedeu o Limite de 30% do Salário. \n Valor da Prestação: R${mensal:.2f}')
print('-=-' * 8)
