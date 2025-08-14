nome = input('Qual o seu nome? ')
while not nome:
    nome = (input("Por favor, digite seu nome: "))
print(f"Olá {nome.capitalize()}")
