"""city = str(input('Informe a Cidade em que Você Nasces: ')).strip()
print(city[:5].upper == 'SANTO')"""

city = input('Digite o nome da cidade: ').split()
print(city[0].upper() == 'SANTO')
