print('Seja bem vindo a fabrica UpCamisetas de Victor Ramalho Dias')
def escolha_modelo():
    global valor
    while True:
        print('Entre com o modelo desejado: ')
        print('   MCS - Manga Curta simples')
        print('   MLS - Manga Longa simples')
        print('   MCE - Manga Curta com estampa')
        print('   MLE - Manga Longa com estampa')
        modelo = input('  Modelo: ')
        if modelo.upper() != 'MCS' and modelo.upper() != 'MLS' and modelo.upper() != 'MCE' and modelo.upper() != 'MLE':
            print('Modelo não disponível. Por favor reinicie a compra!\n')
            continue
        else: #Atribuindo os valores de cada modelo
            if modelo.upper() == 'MCS':
                valor = 1.80
            elif modelo.upper() == 'MLS':
                valor = 2.10
            elif modelo.upper() == 'MCE':
                valor = 2.90
            elif modelo.upper() == 'MLE':
                valor = 3.20
            break


def num_camisetas():
    while True:
        try: #Tente executar:
            camisetas = int(input('Quantas camisetas? '))
            break
        except ValueError: #Se der esse erro (dado não esperado) execute isso:
            print('Número inválido, tente novamente: ')

    while camisetas > 20000:
        camisetas = int(input('Quantidade inválida! Tente outra:'))

    if camisetas < 1:  # aqui "pega" os negativos
        return 'Quantidade inválida!'
    elif camisetas < 20:
        return camisetas
    elif camisetas < 200:
        return camisetas * 0.95
    elif camisetas < 2000:
        return camisetas * 0.93
    elif camisetas <= 20000:
        return camisetas * 0.88


def frete():
    print('Escolha o tipo de frete: ')
    print('1 - Frete por transportadora  = R$100')
    print('2 - Frete por sedex           = R$200')
    print('0 - Retirar pedido na fábrica = R$0')
    escolha_frete = int(input(' '))
    while (escolha_frete != 1) and (escolha_frete !=2) and (escolha_frete !=0): #Barra os números diferentes de 1, 2 ou 0
        escolha_frete = int(input('Escolha o tipo de frete: '))
    if escolha_frete == 1:
        return 100
    elif escolha_frete == 2:
        return 200
    elif escolha_frete == 0:
        return 0

escolha_modelo()
quantidade_camisetas = num_camisetas() #ja chama a função imprimindo o return dentro da var
fret = frete() # mesma coisa, ja chama o frete(), mandando o return para fret

total = (valor * quantidade_camisetas) + fret
print(f'Total a pagar = R${total:.2f} (Modelo: {valor} x Quantidade(com desconto): R${quantidade_camisetas} + frete: {fret}')
