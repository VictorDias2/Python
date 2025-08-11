# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário:

print("-" * 4 + " CLASSIFICANDO UM TRIÂNGULO: " + "-" * 4)
lado1 = int(input("Digite o tamanho do 1º lado: "))
lado2 = int(input("Digite o tamanho do 2º lado: "))
lado3 = int(input("Digite o tamanho do 3º lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <=0:
    print("Os valores fornecidos não formam um triângulo")
elif lado1 != lado2 != lado3 != lado1:
    print("Os valores fornecidos formam um triângulo Escaleno")
elif lado1 == lado2 == lado3:
    print("Os valores fornecidos formam um triângulo Equilátero")
else:
    print("Os valores fornecidos foram um triângulo Isósceles")
