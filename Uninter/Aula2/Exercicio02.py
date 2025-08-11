# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar sabendo que o carro custa R$ 60 por dia e 15 centavos por km rodado:

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual a quilometragem percorrida pelo carro? '))
aluguel = dias*60 + 0.15*km
print(f'O preço a pagar é de {aluguel}. Sendo R$60 por dia (foram {dias}) e 15 centavos por km (foram {km})')
