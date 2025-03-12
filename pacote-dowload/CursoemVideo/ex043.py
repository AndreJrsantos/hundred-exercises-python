peso = float(input('Informe seu Peso (Kg): '))
altura = float(input('Informe sua Altura: '))
if altura.is_integer():
    altura = altura / 100
imc = (peso / altura ** 2)
print(f'Seu IMC (Indíce de Massa Corporal é {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('Você está no PESO IDEAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está OBESO')
elif imc <= 60000:
    print('Você está com OBESIDADE MÓRBIDA')
else:
    print('Você é um objeto super-massivo. A matéria ao seu redor corre risco de colapsar sob sua massa '
          'formando um buraco negro.')
