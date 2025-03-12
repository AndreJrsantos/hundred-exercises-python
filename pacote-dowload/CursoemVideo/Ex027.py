nome = str(input('Digite seu Nome Completo: ')).upper().strip()
nomes = nome.split()
print('Muito Prazer em Te Conhecer, {}!'.format(nome))
print('Seu Primeiro Nome é: {}'.format(nomes[0]))
print('Seu Último Nome é: {}'.format(nomes[len(nomes)-1]))

"""nome = str (input('Digite seu nome completo: ')).upper().strip()
print('O nome é : {}'.format(nome))
print('O primeiro nome é {}'.format(nome[:nome.find(' ')]))
print('O último nome é {}'.format(nome[nome.rfind(' ')+1:]))"""

"""print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu último nome é: {}'.format(nome.split()[-1]))"""
