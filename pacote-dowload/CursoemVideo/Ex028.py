from random import randint
from time import sleep
r = '1'
while r == '1':
    print('\033[4;31m=-=' * 20, '\033[m')
    print(' \033[34mVou \033[4mPensar em um \033[4mNúmero entre \033[4m0 a 5.\033[m')
    print(' \033[1;36mTente adivinhar...\033[m')
    print('\033[4;31m=-=' * 20, '\033[m')
    n = randint(0, 5)
    num = int(input('\033[1;34mEm que Número você acha que Eu Pensei? \n -> \033[m'))
    print('\033[1;31mProcessando...\033[m')
    sleep(2)
    if num == n:
        print(f'\033[1; 33mVOCÊ GANHOU, PARABÉNS!\033[m')
        print(f'\033[37mEu Pensei no Número: {n}\033[m')
    else:
        print(f'\033[1;32mHAHAHA VOCÊ PERDEU!\033[m')
        print(f'\033[37mEu Pensei no Número: {n}\033[m')

    sleep(4)
    print('\033[4;31m========================\033[m')
    print('\033[1;32m [1] Jogar Novamente\033[1;31m \n [2] Fechar Jogo\033[m')
    r = str(input('\033[35m-> \033[m'))
print('\033[4;30mFechando Jogo...\033[m')