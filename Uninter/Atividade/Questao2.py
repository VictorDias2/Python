print('-'*5 + ' Seja muito Bem Vindo a Marmibusiness de Victor Ramalho Dias ' + '-' * 5)
print('-'*31 + ' Cardápio: ' + '-' * 29)
print('-' * 71)
print('-----|   Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)   |-----')
print('-----|      P     |        R$16,00       |        R$15,00        |-----')
print('-----|      M     |        R$18,00       |        R$17,00        |-----')
print('-----|      G     |        R$22,00       |        R$21,00        |-----')
print('-' * 71)

valor = 0.0
while True:
        #Escolhas:
    sabor = input('Escolha o sabor: (BA/FF) ')
    if sabor.upper() != 'BA' and sabor.upper() != 'FF': #Executável apenas com BA ou FF
        print('Sabor não disponível. Por favor reinicie a compra!')
        break
    tamanho = input('Escolha o tamanho: (P/M/G) ')
    if tamanho.upper() != 'P' and tamanho.upper() != 'M' and tamanho.upper() != 'G': #Barramento caso seja um tamanho inválido
        print('Tamanho não disponível. Por favor reinicie a compra!')
        break

        #Mostrar valores e soma-los:
    if sabor.upper() == 'BA':
        if tamanho.upper() == 'P':
            print('Você pediu um Bife Acebolado tamanho P: R$16,00')
            valor += 16.00
        elif tamanho.upper() == 'M':
            print('Você pediu um Bife Acebolado tamanho M: R$18,00')
            valor += 18.00
        elif tamanho.upper() == 'G':
            print('Você pediu um Bife Acebolado tamanho G: R$22,00')
            valor += 22.00

    else:
        if tamanho.upper() == 'P':
            print('Você pediu um Filé de Frango tamanho P: R$15,00')
            valor += 15.00
        elif tamanho.upper() == 'M':
            print('Você pediu um Filé de Frango no tamanho M: R$17,00')
            valor += 17.00
        elif tamanho.upper() == 'G':
            print('Você pediu um Filé de Frango no tamanho G: R$21,00')
            valor += 21.00

        #Continuar a compra:
    continuar = input('-'*30 + '\nDeseja mais alguma marmita? (S/N) ')
    if continuar.upper()[0] == 'S':
        continue
    elif continuar.upper()[0] == 'N':
        print(f'O valor total a ser pago: R${valor}')
        break
    else:
        print('Resposta inválida!')
        break
