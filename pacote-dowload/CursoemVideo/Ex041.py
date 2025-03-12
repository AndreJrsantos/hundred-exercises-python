from datetime import date
ano = int(input('Informe seu Ano de Nascimento: '))
idade = date.today().year - ano
print(f'O Atleta têm {idade} anos.')
if idade <= 9:
    print(f'Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Classificação: MASTER')
