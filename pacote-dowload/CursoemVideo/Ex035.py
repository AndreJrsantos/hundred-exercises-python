a = float(input('Digite o Comprimento da 1° reta: '))
b = float(input('Digite o Comprimento da 2° reta: '))
c = float(input('Digite o Comprimento da 3° reta: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('FORMA UM TRIÂNGULO!')
else:
    print('NÃO FORMA UM TRIÂNGULO!')
