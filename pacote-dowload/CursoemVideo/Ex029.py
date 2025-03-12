vel = float(input('Velocidade do Carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f' Você ULTRAPASSOU o LIMITE DE VELOCIDADE (80km/h)! \n MULTA R$: {multa:.2f}')
else:
    print('Você está DENTRO do LIMITE DE VELOCIDADE!')
print('Tenha Bom Dia! Dirija com Segurança!')
