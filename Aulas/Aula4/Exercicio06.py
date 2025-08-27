# Escreva um algoritmo que leia números, apenas valores positivos devem ser aceitos pelo programa.
# A execução finaliza quando o valor 0 for enviado:

cont, soma = 0, 0
n = int(input('Digite o 1º número para calcular a média: '))
while True:
    if n == 0:
        break
    elif n < 0:
        n = int(input('Não aceitamos números menores que 0! Digite outro: '))
    elif n >= 0:
        soma += n
        cont += 1
        n = int(input(f'{n} foi adicionado. Digite o {cont+1}º valor: '))
        continue

print(f'A média calculada foi = {soma/cont}')
