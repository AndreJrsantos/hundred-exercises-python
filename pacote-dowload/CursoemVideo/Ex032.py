from datetime import date
ano = int(input('Informe o Ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É UM ANO BISSEXTO! =)')
else:
    print('NÃO É UM ANO BISSEXTO! =(')

print(date.today())
print(date.today().year)
print(date.today().month)
print(date.today().day)
print(date.today().ctime())

