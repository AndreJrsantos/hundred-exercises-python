import datetime
data = datetime.date.today().year
maioridade = 0
menoridade = 0

for c in range(1, 8):
    ano_nasc = int(input(f'Ano de Nascimento da {c}° Pessoa: '))
    idade = data - ano_nasc
    if idade >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print(f'Maioridade: {maioridade} pessoas!')
print(f'Menor de Idade: {menoridade} pessoas!')

