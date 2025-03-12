from colorama import Fore
'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu Sexo: [M/F]')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Resposta Inválida! Tente Novamente!')
    else:
        print(Fore.CYAN + f'Seu Sexo {sexo} foi Registrado com Sucesso!' + Fore.RESET)'''

sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos. Por Favor, informe seu Sexo: [M/F]')).strip().upper()[0]
print(Fore.CYAN + f'Sexo {sexo} Registrado com Sucesso!' + Fore.RESET)
