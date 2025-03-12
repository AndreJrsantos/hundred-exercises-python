lista = []
while True:
    n = int(input('Digite um Valor: '))
    while n in lista:
        print(f"O Número {n} já foi digitado!")
        n = int(input('Digite um Valor: '))
    lista.append(n)

    resposta = str(input('Quer continuar? [S/N] \n-> ')).upper().strip()[0]
    if "N" in resposta:
        break

print(f'Foram Digitados {len(lista)} Números')
lista.sort(reverse=True)
print(f'Lista em Ordem Decrescente: \n{lista}')

if 5 in lista:
    print(f'O Valor 5 está na Lista e Aparece {lista.count(5)} vezes')
else:
    print(f'O Valor 5 não foi encontrado na Lista')






'''c = 0
print('\033[4m(type stop to exit)\033[m')
while True:
    c += 1
    n = str(input(f'\n{c}° Number → ')).strip().lower()
    if n == '':
        print('\033[31mType a number. \033[m', end='')
        c -= 1
    elif n == 'stop' and nl == []:
        print('Bye')
        stop = True
        break
    elif n == 'stop':
        stop = False
        c -= 1
        break
    elif '.' in n:
        print('\033[31mYou can not\033[m type float numbers', end='')
        c -= 1
    else:
        n = int(n)
        if c == 1 or n > nl[-1]:
            nl.append(n)
            print(f'({n} added to the position: -1) → list 1')
        else:
            p = 0
            while True:
                if n <= nl[p]:
                    nl.insert(p, n)
                    print(f'({n} added to the position: {p}) → list 1')
                    break
                p += 1
        if c == 1 or n < nl2[-1]:
            nl2.append(n)
            print(f'({n} added to the position: -1) → list 2')
        else:
            p = 0
            while True:
                if n >= nl2[p]:
                    nl2.insert(p, n)
                    print(f'({n} added to the position: {p}) → list 2')
                    break
                p += 1
if not stop:
    if 5 in nl and 5 in nl2:
        print('\nThe number five was \033[32mfound\033[m in both of those lists\n      Position at List 1: ', end='')
        for p, n in enumerate(nl):
            if n == 5:
                print(p, end=' ')
        print('\n      Position at List 2: ', end='')
        for p, n in enumerate(nl2):
            if n == 5:
                print(p, end=' ')
    else:
        print('The number five was \033[31mnot found\033[m in any of those lists')
    print(f'\nLists:\n      List 1: {nl}\n      List 2: {nl2}\nYou typed {c} numbers')'''