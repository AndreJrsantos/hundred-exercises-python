print('~=~' * 13)
print(f'{"BANCO JÚNIORS":^39}')
print('~=~' * 13)
saque = int(input('Informe o Valor que Deseja Sacar: '))
total = saque
céd = 200
totaldecéd = 0
while True:
    if total >= céd:
        total -= céd
        totaldecéd += 1
    else:
        if totaldecéd > 0:
            print(f'Cédulas de R${céd}: {totaldecéd}')
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totaldecéd = 0
        if total == 0:
            break
#################################################################
valorSacado = int(input('Informe o Valor que Deseja Sacar: '))
resto = valorSacado
céd50 = céd10 = céd1 = 0

if resto >= 50:
    céd50 = resto // 50
    resto = resto % 50
if (resto < 50) and (resto >= 10):
    céd10 = resto // 10
    resto = resto % 10
if (resto < 10) and (resto >= 1):
    céd1 = resto // 1
    resto = resto % 1
print(f'Cédulas de R$50: {céd50} \nCédulas de R$10: {céd10} \nCédulas de R$1: {céd1}')