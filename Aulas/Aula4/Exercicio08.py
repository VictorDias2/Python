# Tabuada:

num = int(input('Digite um número para exibir sua tabuada: '))
cont = 1
for i in range(1, 11):
    print(f'{num} x {cont} = {num*cont}')
    cont += 1