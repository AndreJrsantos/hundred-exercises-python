from datetime import date
ano_nasc = int(input('Informe o Seu Ano de Nascimento: '))
idade = date.today().year - ano_nasc
print(f'Você NASCEU em {ano_nasc} e Têm {idade} Anos de Idade em {date.today().year}')
if idade < 18:
    tempo = 18 - idade
    print('Você Não tem Idade para se Alistar!')
    print(f'Em {tempo} Anos você Deverá se Apresentar ao Exército!')
    print(f'Seu Alistamento será no Ano de {date.today().year + tempo}')
elif idade == 18:
    print('Você Deve se Apresentar ao Exército, IMEDIATAMENTE!')
else:
    tempo = idade - 18
    print(f'Você Deveria ter se Apresentado ao Exército em {tempo} anos!')
    print(f'Seu alistamento foi no Ano de {date.today().year - tempo}')

