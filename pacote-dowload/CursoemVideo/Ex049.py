print("------------------")
print("     TABUADA      ")
print("------------------")
num = int(input("Digite um Número: "))
print("-----------------")
for C in range(0, 11):
    r = (num * C)
    print(f"| {num} X {C:<2} = {r:<4} |")
print("-----------------")
