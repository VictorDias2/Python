# Escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado.

def fatorial(num):
    fat = 1
    if num == 0:
        return 1
    for i in range(1, num+1, 1):
        fat *= i
    return fat
x = int(input('Digite um número para calcular seu fatorial: '))
print(f'{x}! = {fatorial(x)}')
