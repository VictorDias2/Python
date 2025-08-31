from random import randint
from time import sleep
print('-' * 23)
print('-' * 7 + ' JOKENPÔ ' + '-' * 7)
print(' ' * 9 + '1 - ✊') # 1 = PEDRA
print(' ' * 9 + '2 - ✋') # 2 = PAPEL
print(' ' * 9 + '3 - ✌️') # 3 = TESOURA
print('-' * 23)
print('Você consegue ganhar de mim? 😎')

resultado = []

for cont in range(0, 3):
    numero_sorteado = randint(1, 3)
    numero_jogado = int(input('  Então jogue: '))
    while numero_jogado != 1 and numero_jogado != 2 and numero_jogado != 3:
        numero_jogado = int(input('Numero indisponível. Jogue novamente: '))
    if numero_jogado == 1:  # Se o jogador jogar PEDRA
        print('Você jogou Pedra, ',end='')
        if numero_sorteado == 1:  # Número sorteado for PEDRA
            sleep(1)
            print(' e eu também kkk')
            sleep(0.4)
            resultado.append('empate')
        elif numero_sorteado == 2:  # Número sorteado for PAPEL
            sleep(1)
            print('mas eu joguei Papel, você perdeu heim!')
            sleep(0.4)
            resultado.append('derrota')
        else:  # Número sorteado for TESOURA
            sleep(1)
            print('e eu jogue Tesoura, dessa vez você ganhou.')
            sleep(0.4)
            resultado.append('vitória')

    elif numero_jogado == 2: # Se o jogador jogar PAPEL
        print('Você jogou Papel, ',end='')
        if numero_sorteado == 1:  # Número sorteado for PEDRA
            sleep(1)
            print('e eu apostei em Pedra. Perdi :/')
            sleep(0.4)
            resultado.append('vitoria')
        elif numero_sorteado == 2:  # Número sorteado for PAPEL
            sleep(1)
            print('é... empatamos heim')
            sleep(0.4)
            resultado.append('empate')
        else:  # Número sorteado for TESOURA
            sleep(1)
            print('eu joguei Tesoura, ganhei haha')
            sleep(0.4)
            resultado.append('derrota')

    else: #Se o jogador jogar TESOURA
        print('Você jogou Tesoura, ', end='')
        if numero_sorteado == 1:  # Número sorteado for PEDRA
            sleep(1)
            print('sabiaa, eu ganhei com a Pedra hehehe')
            sleep(0.4)
            resultado.append('derrota')
        elif numero_sorteado == 2:  # Número sorteado for PAPEL
            sleep(1)
            print('agora eu perdi kkk')
            sleep(0.4)
            resultado.append('vitoria')
        else:  # Número sorteado for TESOURA
            sleep(1)
            print('hmm, também joguei Tesoura!')
            sleep(0.4)
            resultado.append('empate')
print(resultado)