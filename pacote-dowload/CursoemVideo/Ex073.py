from time import sleep
brasileirao = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Athletico-PR',
               'São Paulo', 'Fluminense', 'Bragantino', 'Fortaleza', 'Internacional',
               'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos', 'Corinthians', 'Goiás',
               'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')
print(f'{" TABELA DO BRASILEIRÃO ":~^30}')
contador = 1
for times in brasileirao:
    print(f'{contador}°  {times.upper()}')
    contador += 1
print('~' * 30)
print()
print(f'{" TABELA DO G5 ":~^30}')
sleep(5)
posicaoG5 = 1
for c in range(0, 5):
    print(f'{posicaoG5}° {brasileirao[c]}')
    posicaoG5 += 1
print('~' * 30)
print()
print(f'{" ÁREA DE REBAIXAMENTO ":~^30}')
sleep(5)
cont = 17
for i in range(-4, 0):
    print(f'{cont}° {brasileirao[i]}')
    cont += 1
print('~' * 30)
print()
print(f'{" ORDEM ALFABÉTICA ":~^30}')
sleep(5)

for times in sorted(brasileirao):
    print(f'{times}')
print('~' * 30)
print(f'O São Paulo está na {brasileirao.index("São Paulo") + 1}° Posição!')
print('~' * 30)
