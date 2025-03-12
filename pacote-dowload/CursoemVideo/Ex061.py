primeiro_termo = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(primeiro_termo, end='-> ')
    primeiro_termo += razao
    c += 1
print('Fim!')
