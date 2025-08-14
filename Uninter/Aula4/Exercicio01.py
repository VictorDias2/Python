# Escreva um algoritmo que imprima na tela somente valores num intervalo especificado pelo usuário: (While)

inicio = int(input('Com qual valor deseja iniciar a contagem? '))
termino = int(input('Com qual valor deseja terminar a contagem? '))
intervalo = int(input('De quantos em quantos números deseja fazer a contagem? '))

if inicio >= termino:
    while inicio >= termino:
        print(inicio)
        inicio -= intervalo
else:
    while inicio <= termino:
        print(inicio)
        inicio += intervalo
