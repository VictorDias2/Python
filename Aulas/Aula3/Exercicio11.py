# Escreva um algoritmo que leia dois valores numéricos e pergunte ao usuário qual operação ele deseja realizar:

v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
op = input("Qual operação deseja fazer: \n + Adição\n - Subtração\n x Multiplicação\n / Divisão\n")

if op == "+":
    print(f"{v1} + {v2} = {v1 + v2}")
elif op == "-":
    print(f"{v1} - {v2} = {v1 - v2}")
elif op == "x":
    print(f"{v1} x {v2} = {v1 * v2}")
elif op == "/":
    print(f"{v1} / {v2} = {v1 / v2:.2f}")
else:
    print("Operação inválida")