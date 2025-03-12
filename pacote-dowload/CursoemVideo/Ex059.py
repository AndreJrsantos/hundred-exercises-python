from colorama import Fore
from time import sleep
print(Fore.YELLOW + f'{" Calculator " :~^40}' + Fore.RESET)
opc = 4
while opc != 5:
    while opc == 4:
        n1 = int(input(Fore.LIGHTYELLOW_EX + 'Primeiro Número: '))
        n2 = int(input('Segundo Número: ' + Fore.RESET))
        print(Fore.CYAN + '~~' * 20)
        opc = int(input('''[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa \n Qual sua Opção? \n-> '''))
        print('~~' * 20 + Fore.RESET)
    if opc == 1:
        print(Fore.LIGHTGREEN_EX + f'A Soma entre {n1} + {n2} é {n1 + n2}' + Fore.RESET)
    elif opc == 2:
        print(Fore.LIGHTBLUE_EX + f'A Multiplicação entre {n1} x {n2} é {n1 * n2}' + Fore.RESET)
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(Fore.LIGHTMAGENTA_EX + f'O Maior Número entre {n1} e {n2} é {maior}' + Fore.RESET)
    elif opc > 5:
        print(Fore.LIGHTRED_EX + f'Opção {opc} inválida. Tente Novamente!' + Fore.RESET)
    print(Fore.CYAN + '~~' * 20)
    opc = int(input('''[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa \n Qual sua Opção? \n-> '''))
    print('~~' * 20 + Fore.RESET)
    sleep(2)
print(Fore.LIGHTRED_EX + 'Saindo do Programa... \nVolte Sempre!' + Fore.RESET)
