n1 = float(input('Informe sua Primeira nota: '))
n2 = float(input('Informe sua Segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print(f' REPROVADO! \n MÉDIA: {m:.1f}')
elif (m >= 5.0) and (m <= 6.9):
    print(f' RECUPERAÇÃO! \n MÉDIA: {m:.1f}')
elif m >= 7.0:
    print(f' APROVADO! \n MÉDIA: {m:.1f}')