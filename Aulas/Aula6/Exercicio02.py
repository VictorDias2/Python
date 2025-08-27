def soma(*num): # * = Tupla que não recebe limite, tamanho qualquer dependendo de quantos dados forem passados como parâmetro
    cont = 0
    print(f'Tupla: {num}')
    for i in num:
        cont += i
    return cont

print(f'Resultado: {soma(1, 2)}\n')
print(f'Resultado: {soma (1, 2, 3, 4, 5, 6, 7, 8, 9)}')
