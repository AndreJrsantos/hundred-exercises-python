from colorama import Fore as f
from random import randint
from time import sleep
print(f.LIGHTYELLOW_EX + '~~' * 20)
print(f'{" Par ou Ímpar ":^40}')
print('~~' * 20 + f.RESET)
nome = str(input(f.LIGHTCYAN_EX + 'NickName: ' + f.RESET)).strip()
espacos = len(nome) + 29
sleep(1)
print(f.LIGHTCYAN_EX + f'Olá {nome}! Seja Muito Bem-Vindo ao')
print(f'{"Game Par ou Ímpar!!!":^{espacos}}' + f.RESET)
cont = 0

while True:
    sleep(1)
    print(f.LIGHTYELLOW_EX + '~~' * 20 + f.RESET)
    ParOuImpar = int(input(f.LIGHTBLUE_EX + '[1] Par \n[2] Ímpar \nEscolha: ' + f.RESET))
    sleep(1.5)
    if ParOuImpar == 1 or ParOuImpar == 2:
        print(f.LIGHTYELLOW_EX + '~~' * 20 + f.RESET)
        jogador = int(input(f.LIGHTBLUE_EX + 'Jogue um Número: ' + f.RESET))
        computador = randint(0, 10)
        soma = jogador + computador
        if ParOuImpar == 1:  # PAR
            print(f.RED + f'{nome} é PAR! \nComputador é ÍMPAR!' + f.RESET)
            sleep(1)
            print(f.LIGHTCYAN_EX + 'PAR')
            sleep(0.5)
            print('OU')
            sleep(0.5)
            print('ÍMPAR!' + f.RESET)
            if (jogador + computador) % 2 == 0:  # Ganha
                sleep(2)
                print(f.LIGHTGREEN_EX + f'Parabéns {nome}, Você Venceu!' + f.RESET)
                sleep(1)
                print(f.YELLOW + f'Computador Jogou: {computador} \n {nome} Jogou: {jogador} \n {computador} + {jogador} = {soma}' + f.RESET)
                sleep(2)
                cont += 1
            else:  # PERDE
                sleep(2)
                print(f.LIGHTRED_EX + 'Que Pena, Você Perdeu!')
                sleep(1)
                print(f.YELLOW + f'Computador Jogou: {computador} \n {nome} Jogou: {jogador} \n {computador} + {jogador} = {soma}' + f.RESET)
                sleep(2)
                break
        elif ParOuImpar == 2:
            print(f.RED + f'{nome} é ÍMPAR! \nComputador é PAR!' + f.RESET)
            sleep(1)
            print(f.LIGHTCYAN_EX + 'PAR')
            sleep(0.5)
            print('OU')
            sleep(0.5)
            print('ÍMPAR!' + f.RESET)
            if (jogador + computador) % 2 != 0:
                sleep(2)
                print(f.LIGHTGREEN_EX + f'Parabéns {nome}, Você Venceu!' + f.RESET)
                sleep(1)
                print(f.YELLOW + f'Computador Jogou: {computador} \n{nome} Jogou: {jogador} \n{computador} + {jogador} = {soma}' + f.RESET)
                sleep(2)
                cont += 1
            else:
                sleep(2)
                print(f.LIGHTRED_EX + 'Que Pena, Você Perdeu!')
                sleep(1)
                print(f.YELLOW + f'Computador Jogou: {computador} \n{nome} Jogou: {jogador} \n{computador} + {jogador} = {soma}' + f.RESET)
                sleep(2)
                break
    else:
        print(f.RED + 'ERRO404! \nOpção Inválida, Tente Novamente!' + f.RESET)
        sleep(1.2)

print(f.LIGHTYELLOW_EX + f'{" PLACAR ":~^40}' + f.RESET)
print(f.LIGHTGREEN_EX + f'{f"Vitórias Consecutivas: {cont}":^40}' + f.RESET)
print(f.LIGHTYELLOW_EX + '~~' * 20 + f.RESET)
sleep(3)
print(f.LIGHTRED_EX + 'JOGO ENCERRADO!' + f.RESET)
