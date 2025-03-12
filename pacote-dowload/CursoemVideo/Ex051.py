primeiro_termo = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
'''for c in range(0, 10):
    print(termo, end='-> ')
    termo += razao'''

print('')
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo + razao, razao):
    print(i, end='-> ')

