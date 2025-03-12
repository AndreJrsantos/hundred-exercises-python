s = float(input('informe seu salário: R$ '))
if s > 1250.00:
    s = s + (s * 0.10)
    print(f'Com o Aumento de 10%, seu salário será de: R$ {s}')
else:
    s = s + (s * 0.15)
    print(f'Com o Aumento de 15%, seu salário será de: R$ {s}')
