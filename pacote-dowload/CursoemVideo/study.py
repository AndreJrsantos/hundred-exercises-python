hello = 'Hello'
world = 'World'
print(f'{hello}, {world}!!!')

b = input('Digite algo: ')
print('O tipo primitivo desse valor é {}!'.format(type(b)))
print('Só tem espaços? ', b.isspace())
print('É um número? ', b.isnumeric())
print('É alfabético? ', b.isalpha())
print('É alfanumérico? ', b.isalnum())
print('Está em maiúsculas? ', b.isupper())
print('Está em minúsculas? ', b.islower())
print('Está capitalizada? ', b.istitle())

# str, int, float

num = int(input('write a number: '))
raiz = float(num ** (1/2))
print(f"A Raiz Quadrada é = {raiz:.2f}") # casas após o ponto/vírgula

print("------------------")
print("     TABUADA      ")
print("------------------")
num = int(input("Digite um Número: "))
c = 0
print("-----------------")
while c <= 10:
    r = (num * c)
    print(f"| {num} X {c:<2} = {r:<4} |")
    c = c + 1
print("-----------------")

print("------------------")
print("  TRIGONOMETRIA   ")
print("------------------")
import math
angulo = float(input("Digite o Ângulo: "))
a = math.radians(angulo)
sen = math.sin(a)
cos = math.cos(a)
tg = math.tan(a)
print(f"O Seno do Ângulo {angulo}° vale {sen:.2f}")
print(f"O Cosseno do Ângulo {angulo}° vale {cos:.2f}")
print(f"A Tangente do Ângulo {angulo}° vale {tg:.2f}")

import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aleatorio = random.choice(lista)
print(aleatorio)

# if, else, elif

# lista[]
# tupla()
# dicionário{}

