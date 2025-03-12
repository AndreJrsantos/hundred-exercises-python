Adultos = Homens = MulheresMenos20 = 0
while True:
    print('--' * 20)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('--' * 20)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] \n->')).upper().split()[0]
    if idade > 18:
        Adultos += 1
    if sexo == 'M':
        Homens += 1
    if sexo == 'F' and idade < 20:
        MulheresMenos20 += 1
    print('--' * 20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] \n->')).upper().split()[0]
    if resposta in 'N':
        break
print('--' * 20)
print(f'Total de Pessoas com Mais de 18 Anos: {Adultos}')
print(f'Total de Homens Cadastrados: {Homens}')
print(f'Mulheres com Menos de 20 Anos: {MulheresMenos20}')
