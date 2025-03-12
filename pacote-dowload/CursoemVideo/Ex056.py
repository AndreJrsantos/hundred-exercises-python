soma_idade = 0
idade_homem = 0
total_mulher = 0
for c in range (1, 5):
    print(f'{f" {c}° PESSOA ":-^35}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if sexo == "M":
        if idade > idade_homem:
            idade_homem = idade
            nome_velho = nome
    else:
        if idade < 20:
            total_mulher += 1
media = soma_idade / 4
print(f'A média de idade do grupo é {media:.1f} anos')
print(f'O homem mais velho tem {idade_homem} anos e se chama {nome_velho}')
print(f'Ao todo são {total_mulher} com menos de 20 anos')

'''lista = []
idade1 = 0
feminino = 0
masculino = 0
maisvelho = 0
maisde20 = 0
nomevelho = []
for c in range(1, 5):
    print('{:=^50}'.format('{}° pessoa'.format(c)))
    nome = str(input( 'Nome da {}° pessoa:'.format(c)))
    idade = int(input('Sua idade:'))
    sexo = str(input('[M/F]:')).upper().strip()
    lista = lista + [idade]
    idade1= idade1 + idade

    if c == 1 and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo =='M' and maisvelho > idade:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'F':
        feminino = feminino + 1
    if sexo == 'F' and idade > 20:
        maisde20 = maisde20+1
    if sexo == 'M':
        masculino = masculino+1

print('a média de idade é {}'.format(idade1/4))
print('A pessoa mais velha tem {} anos e se chama {} '.format(max(lista),nomevelho))
print('Ao todo, temos {} mulher(es) e {} dela(s) tem mais de 20 anos'.format(feminino,maisde20,end=''))
print('E {} homen(s)'.format(masculino))'''