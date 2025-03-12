dist = float(input('Informe a Distância da Viagem (em Km): '))
if dist <= 200:
    v_pass = dist * 0.50
else:
    v_pass = dist * 0.45
print(f'O Valor da Passagem será: R${v_pass:.2f}')
