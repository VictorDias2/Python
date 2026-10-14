
estoque = {
    1: {'nome': 'Papel A4', 'quantTotal': 1300},
    2: {'nome': 'Caneta Azul', 'quantTotal': 52},
    3: {'nome': 'Caderno', 'quantTotal': 12},
    4: {'nome': 'Grampeador', 'quantTotal': 36},
    5: {'nome': 'Mouse', 'quantTotal': 27},
    6: {'nome': 'Teclado', 'quantTotal': 9}
}
#Repete até selecionar '4'(encerrar programa)
while True:
      print('====== MENU ======'
            '\n1 - Entrada'
            '\n2 - Saída'
            '\n3 - Mostrar estoque'
            '\n4 - Sair\n')
      opcao = int(input())

                        #ENTRADA:
      if opcao == 1:
            print('=== PRODUTOS ===')
            print('1 - Papel A4')
            print('2 - Caneta Azul')
            print('3 - Caderno')
            print('4 - Grampeador')
            print('5 - Mouse')
            print('6 - Teclado')

            cod = int(input('Informe o código para adicionar o produto: '))

            #Se tiver o codigo no estoque, faça:
            if cod in estoque:
                  quantRecebida = int(input('Informe a quantidade recebida: '))
                  data = input('Informe a data da entrada: ')
                  responsavel = input('Informe o nome do responsavel do produto: ')

                  estoque[cod]['quantTotal'] += quantRecebida
                  print(f'\nEntrada do produto nº{cod} registrada com sucesso em {data} por {responsavel}!\n')

                  # Estoque novo:
                  print('Estoque atualizado:')
                  for produto in estoque.values():
                        print(f"Produto: {produto['nome']}")
                        print(f"Quantidade: {produto['quantTotal']}\n")

            else:
                  print('Código de produto inválido!')


                        #SAIDA:
      elif opcao == 2:
            print('=== PRODUTOS ===')
            print('1 - Papel A4')
            print('2 - Caneta Azul')
            print('3 - Caderno')
            print('4 - Grampeador')
            print('5 - Mouse')
            print('6 - Teclado')

            codigo = int(input('Informe o código para retirar o produto: '))

            # Se tiver o codigo no estoque, faça:
            if codigo in estoque:
                  quantRetirada = int(input('Informe a quantidade retirada: '))

                  #Verifica a quantidade:
                  if quantRetirada > estoque[codigo]['quantTotal']:
                        print("Não há quantidades suficientes!")
                  else:
                        data = input('Informe a data de retirada: ')
                        responsavel = input('Informe o nome do responsavel do produto: ')
                        estoque[codigo]['quantTotal'] -= quantRetirada
                        print(f'\nSaída do produto nº{codigo} retirada com sucesso em {data} por {responsavel}!\n')

                              # Estoque novo:
                        print('Estoque atualizado:')
                        for produto in estoque.values():
                              print(f"Produto: {produto['nome']}")
                              print(f"Quantidade: {produto['quantTotal']}\n")


            else:
                  print('Código de produto inválido!')
                        #MOSTRAR ESTOQUE:
      elif opcao == 3:
            print('Estoque atualizado:')
            for produto in estoque.values():
                  print(f"Produto: {produto['nome']}")
                  print(f"Quantidade: {produto['quantTotal']}\n")

                        #SAIR:
      elif opcao == 4:
            break

print('Programa encerrado!')
