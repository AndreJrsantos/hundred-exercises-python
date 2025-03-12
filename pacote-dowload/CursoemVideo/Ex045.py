from random import randint
from time import sleep
print('\033[31m=' * 40, '\033[m')
print(f'\033[36m{" JOKENPÔ GAME ":=^40}\033[m')
print('\033[31m=' * 40, '\033[m')
nome = input('\033[33mInsira um NickName: \033[m').strip().upper()
print('\033[31m=' * 40, '\033[m')
resp = 1
point_Player = 0
point_Computer = 0
empates = 0
itens = ['Pedra', 'Tesoura', 'Papel']
while resp == 1:
    print(f'''\033[34m{nome} Escolha sua Jogada:\033[m
    \033[37m[0] PEDRA \033[m
    \033[35m[1] TESOURA \033[m
    [2] PAPEL''')
    player = int(input('-> '))
    computador = randint(0, 2)
    print('\033[33mComputador Escolhendo Sua Opção...\033[m')
    sleep(1.8)
    print('\033[1;31mJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!\033[m')
    sleep(1)
    if player == 0 and computador == 1: #PEDRA
        print('\033[1;32mVitória!!!\033[m')
        point_Player = point_Player + 1
    elif player == 1 and computador == 2: #TESOURA
        print('\033[1;32mVitória!!!\033[m')
        point_Player = point_Player + 1
    elif player == 2 and computador == 0: #PAPEL
        print('\033[1;32mVitória!!!\033[m')
        point_Player = point_Player + 1
    elif player == computador:
        print('\033[1;33mEmpate!!!\033[m')
        empates = empates + 1
    else:
        print('\033[1;31mDerrota!!!\033[m')
        point_Computer = point_Computer + 1
    sleep(1.5)

    print(f'\033[34mComputador Jogou {itens[computador]}!')
    print(f'{nome} Jogou {itens[player]}!\033[m')

    sleep(1.5)
    print('\033[31m=' * 40, '\033[m')
    print(f'\033[36m{f"PLACAR DE {nome}":=^40}\033[m')
    print(f'\033[1;32m Vitórias = {point_Player} \n \033[1;31mDerrotas = {point_Computer} \n \033[1;33mEmpates  = {empates}')
    print('\033[31m=' * 40, '\033[m')
    sleep(2.3)
    resp = int(input('\033[34m [1] Jogar Novamente! \n [2] Fechar Jogo! \n -> \033[m'))
print('\033[31m=' * 40, '\033[m')
print('\033[31mFechando...')
sleep(1.2)
print('Fechado!\033[m')
