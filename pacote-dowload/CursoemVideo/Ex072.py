numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze/Catorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um Número entre 0 e 20: '))
        if (num >= 0) and (num <= 20):
            break
    print(f'Seu Número Por Extenso é {numeros[num]}')
    resp = str(input("Quer Continuar? [S/N] \n-> ")).upper().strip()[0]
    if resp in 'N':
        break
print('Fim')
