# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 - 1 e 100 inclusos? (For)
soma, cont = 0, 0
print("A média dos números: ")

for num in range(2, 101, 2):
    print(num, end=', ')
    soma += num
    cont += 1
print(f"\nÉ de {soma/cont:.0f}")

