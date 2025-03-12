print("------------------")
print("     TABUADA      ")
print("------------------")
num = int(input("Digite um Número: "))
c = 0
print("-----------------")
while c <= 10:
    r = (num * c)
    print(f"| {num} X {c:<2} = {r:<4} |")
    c = c + 1

print("-----------------")
