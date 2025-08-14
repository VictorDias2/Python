# Escreva um algoritmo que calcule a sua média de notas (5 no total) em determinada disciplina: (While)

n, media = 1,0
while n <= 5:
    soma = (float(input(f'Escreva a nota {n}: ')))
    n += 1
    media += soma
print(f"A média das notas é de {media/(n-1)}")
