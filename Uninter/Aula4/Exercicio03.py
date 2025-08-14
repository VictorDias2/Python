# Crie um algoritmo que receba somente algum valor maior que 0:

v,n = 0,0
while v <= 0:
    v = int(input('Envie qualquer valor que seja maior que 0: '))
    n +=1
if n == 2:
    print(f'Depois de apenas 1 tentativa? Thanks!')
elif n > 2:
    print(f'Depois de {n} tentativas? Poderia ser mais rápido, né?')
else:
    print("Very Good, Thanks!")
