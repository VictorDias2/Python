while True:
    try: #Tente executar:
        x = int(input('Digite um número: '))
        break
    except ValueError: #Se der esse erro (dado não esperado) execute isso:
        print('Oops! Número inválido, tente novamente: ')
