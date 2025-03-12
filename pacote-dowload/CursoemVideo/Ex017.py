import math
'''CatOposto = float(input("Informe o comprimento do Cateto Oposto: "))
CatAdj = float(input("Informe o comprimento do Cateto Adjacente: "))
Hip = math.hypot(CatOposto , CatAdj)
print(f"O comprimento da Hipotenusa Vale: {Hip:.2f}")'''

CatOposto = float(input("Informe o comprimento do Cateto Oposto: "))
CatAdj = float(input("Informe o comprimento do Cateto Adjacente: "))
Hip = math.sqrt(pow(CatAdj, 2) + pow(CatOposto, 2))
print(f"O comprimento da Hipotenusa Vale: {Hip:.2f}")



'''co = float(input("Informe o comprimento do Cateto Oposto: "))
ca = float(input("Informe o comprimento do Cateto Adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"O comprimento da Hipotenusa Vale: {hi:.2f}")'''