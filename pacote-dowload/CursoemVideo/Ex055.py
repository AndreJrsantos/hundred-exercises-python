maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso = float(input(f"Digite o Peso da {c}° Pessoa (kg): "))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

print(f' O Maior Peso foi {maior_peso} Kg \n O Menor Peso foi {menor_peso} Kg')
