from colorama import init, Fore, Style
from random import randint
from time import sleep
init()
print(Fore.RED + '=' * 40 + Fore.RESET)
print(Fore.CYAN + f'{" JOKENPÔ GAME ":=^40}' + Fore.RESET)
print(Fore.RED + '=' * 40 + Fore.RESET)
nome = input(Fore.YELLOW + 'Insira um NickName: ' + Fore.RESET).strip().upper()
print(Fore.RED + '=' * 40 + Fore.RESET)
resp = 1
point_Player = 0
point_Computer = 0
empates = 0
itens = ['Pedra', 'Tesoura', 'Papel']
while resp == 1:
    print(Fore.BLUE + f'{nome} Escolha sua Jogada:' + Fore.RESET, Fore.BLACK + ' \n [0] PEDRA' + Fore.RESET, Fore.MAGENTA + ' \n [1] TESOURA' + Fore.RESET, '\n [2] PAPEL')
    player = int(input('-> '))
    computador = randint(0, 2)
    print(Fore.YELLOW + 'Computador Escolhendo Sua Opção...' + Fore.RESET)
    sleep(1.8)
    print(Fore.RED + 'JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!' + Fore.RESET)
    sleep(1)
    if player == 0 and computador == 1: #PEDRA
        print(Fore.GREEN + 'Vitória!!!' + Fore.RESET)
        point_Player = point_Player + 1
    elif player == 1 and computador == 2: #TESOURA
        print(Fore.GREEN + 'Vitória!!!' + Fore.RESET)
        point_Player = point_Player + 1
    elif player == 2 and computador == 0: #PAPEL
        print(Fore.GREEN + 'Vitória!!!' + Fore.RESET)
        point_Player = point_Player + 1
    elif player == computador:
        print(Fore.YELLOW + 'Empate!!!' + Fore.RESET)
        empates = empates + 1
    else:
        print(Fore.RED + 'Derrota!!!' + Fore.RESET)
        point_Computer = point_Computer + 1
    sleep(1.5)

    print(Fore.BLUE + f'Computador Jogou {itens[computador]}!')
    print(f'{nome} Jogou {itens[player]}!' + Fore.RESET)

    sleep(1.5)
    print(Fore.RED + '=' * 40 + Fore.RESET)
    print(Fore.CYAN + f'{f"PLACAR DE {nome}":=^40}' + Fore.RESET)
    sleep(1)
    print(Fore.GREEN + f' Vitórias = {point_Player}' + Fore.RESET, Fore.RED + f'\n Derrotas = {point_Computer}' + Fore.RESET, Fore.YELLOW + f'\n Empates  = {empates}' + Fore.RESET)
    print(Fore.RED + '=' * 40 + Fore.RESET)
    sleep(2.3)
    resp = int(input(Fore.BLUE + ' [1] Jogar Novamente! \n [2] Fechar Jogo! \n -> ' + Fore.RESET))
print(Fore.RED + '=' * 40 + Fore.RESET)
print(Fore.RED + 'Fechando...')
sleep(1.2)
print('Fechado!' + Fore.RESET)

''' ---------------------------------------------------------------------
    | Constante         | Descrição                                      |
    ---------------------------------------------------------------------
    | Fore.BLACK        | Texto em preto                                 |
    | Fore.RED          | Texto em vermelho                               |
    | Fore.GREEN        | Texto em verde                                 |
    | Fore.YELLOW       | Texto em amarelo                               |
    | Fore.BLUE         | Texto em azul                                   |
    | Fore.MAGENTA      | Texto em magenta                               |
    | Fore.CYAN         | Texto em ciano                                 |
    | Fore.WHITE        | Texto em branco                                 |
    | Fore.RESET        | Redefine a cor do texto ao padrão               |
    | Back.BLACK        | Fundo em preto                                 |
    | Back.RED          | Fundo em vermelho                               |
    | Back.GREEN        | Fundo em verde                                 |
    | Back.YELLOW       | Fundo em amarelo                               |
    | Back.BLUE         | Fundo em azul                                   |
    | Back.MAGENTA      | Fundo em magenta                               |
    | Back.CYAN         | Fundo em ciano                                 |
    | Back.WHITE        | Fundo em branco                                 |
    | Back.RESET        | Redefine o fundo ao padrão                      |
    | Style.DIM         | Texto com estilo de cor mais fraca              |
    | Style.NORMAL      | Texto com estilo normal                         |
    | Style.BRIGHT      | Texto com estilo mais brilhante                 |
    | Style.RESET_ALL   | Redefine todas as configurações de estilo       |
    ------------------------------------------------------------------------'''

