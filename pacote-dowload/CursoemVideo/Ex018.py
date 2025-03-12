import math
an = float(input("Digite o Ângulo: "))
a = math.radians(an)
sen = math.sin(a)
cos = math.cos(a)
tg = math.tan(a)
print(f"O Seno do Ângulo {an}° vale {sen:.2f}")
print(f"O Cosseno do Ângulo {an}° vale {cos:.2f}")
print(f"A Tangente do Ângulo {an}° vale {tg:.2f}")