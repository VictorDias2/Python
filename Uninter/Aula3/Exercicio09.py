# Se ano é divisível por 4, escreva que o ano é bissexto, caso contrário o ano não é bissexto:

ano = int(input("Qual ano? "))
if ano % 4 == 0:
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} NÃO é um ano bissexto!")
