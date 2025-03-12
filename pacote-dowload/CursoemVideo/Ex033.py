n1 = int(input('Digite o Primeiro Número:'))
n2 = int(input('Digite o Segundo Número:'))
n3 = int(input('Digite o Terceiro Número:'))
maior = n1
menor = n1
#Verificando o Menor
if n1 != n2 or n2 != n3:
    if (n2 < n1) and (n2 < n3):
        menor = n2
    elif (n3 < n1) and (n3 < n2):
        menor = n3
    #Verificando o Maior
    elif (n2 > n1) and (n2 > n3):
        maior = n3
    elif (n3 > n1) and (n3 > n2):
        maior = n3
    print(f'O {maior} é o MAIOR número e o {menor} é o MENOR número!')
else:
    print('Os três números digitados são iguais!')
