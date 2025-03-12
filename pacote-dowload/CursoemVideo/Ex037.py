print('_' * 30)
print('''Selecione a Base de Conversão:
 [1] Binário
 [2] Octal
 [3] Hexadecimal ''')
base = int(input('-> '))
print('-' * 30)
n = int(input('Informe o Número para Conversão: '))
if base == 1:
    print(f'{n} convertido para Binário é {bin(n)[2:]}')
elif base == 2:
    print(f'{n} convertido para Octal é {oct(n)[2:]}')
elif base == 3:
    print(f'{n} convertido para Hexadecimal é {hex(n)[2:]}')
else:
    print(' !!!Erro!!! \n Base de Conversão Inválida! \n Tente Novamente!')