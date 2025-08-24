i = 1
while True:
    try:
        nome = input ( 'Por favor digite o seu nome: ')
        ind = int ( input ( 'Digite um índice do seu nome digitado: '))
        print(nome[ind-1])
        break

    except ValueError:
        print('Oops! Nome inválido. Tente novamente...')
    except IndexError:
        print('Oops! índice inválido. Tente novamente...')

    finally: #sempre executa, independente da tentativa ou exceções.
        print(f'Tentativa {i}')
        i += 1
