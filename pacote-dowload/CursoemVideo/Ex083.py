# minha tentativa
"""lista_expressão = [str(input('Digite sua Expressão: ')).strip()]
abre = fecha = 0
for c, i in enumerate(lista_expressão):
    if i == "(":
        abre += 1
    elif i == ")":
        fecha += 1
print(abre)
print(fecha)

if abre == fecha:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')"""

expressao = str(input('Digite a Expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')
