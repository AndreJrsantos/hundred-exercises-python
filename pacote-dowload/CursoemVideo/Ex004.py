b = input('Digite algo: ')
print('O tipo primitivo desse valor é {}!'.format(type(b)))
print('Só tem espaços? ', b.isspace())
print('É um número? ', b.isnumeric())
print('É alfabético? ', b.isalpha())
print('É alfanumérico? ', b.isalnum())
print('Está em maiúsculas? ', b.isupper())
print('Está em minúsculas? ', b.islower())
print('Está capitalizada? ', b.istitle())
