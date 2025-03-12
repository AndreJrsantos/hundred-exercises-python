a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print(f'Os Segmentos {a}, {b} e {c} FORMAM UM TRIÂNGULO!')
    if a == b and b == c: #a == b == c
        print('\033[33mTipo: EQUILÁTERO\033[m')
    elif a == b or b == c or a == b:
        print('\033[33mTipo: ISÓSCELES\033[m')
    elif a != b and b != c:
        print('\033[33mTipo: ESCALENO\033[m')
else:
    print('\033[31m!!!Erro444!!!\033[m \nNÃO FORMA UM TRIÂNGULO!\n Tente Novamente!')