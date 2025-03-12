import pygame
import colorama
print("----------------")
print("Escolha A Música")
print("----------------")
print("[1] Yellow \n[2] Viva La Vida")
resp = input('-> ')
print("----------------")

if resp == '1':
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('yellow.mp3')
    pygame.mixer_music.play()
    print("Tocando Yellow...")
else:
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('vivalavida.mp3')
    pygame.mixer_music.play()
    print("Tocando Viva La Vida...")

input(colorama.Fore.BLUE + 'Pressione a Tecla "Espaço" para Terminar a Reprodução! \n -> ' + colorama.Fore.RESET)
if resp == " ":
    pygame.event.clear()
print('Encerrado!')
