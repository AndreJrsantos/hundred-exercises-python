primeiro_termo = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(primeiro_termo, end='-> ')
        primeiro_termo += razao
        c += 1
    print('Pausa!')
    mais = int(input('Quantos termos a mais? '))
print(f'FIM! \nPA com {total} Termos')



'''primeiro_termo = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
c = 1
while c <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    c += 1
print('...')
termos = int(input('Mais quantos Termos quer Analisar: '))
qnt_termos = 11 + termos
while termos != 0:
    while c < qnt_termos:
        print(f'{termo}', end=' -> ')
        termo += razao
        c += 1
    print('...')
    termos = int(input('Mais quantos Termos quer Analisar: '))
    qnt_termos += termos

print(f'PA Finalizada com {qnt_termos - 1} Termos!')'''
