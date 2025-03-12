dias = int(input("Quantos Dias ficou com o Carro? "))
km = float(input("Quantos Km percorreu? "))
valor = (dias * 60) + (km * 0.15)
print(f"O preço a se pagar é {valor:.2f} reais!")