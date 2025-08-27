# Escreva uma função que calcule o quadrado de um número recebido como parâmetro e retorne o seu resultado.
# Faça uma validação dos dados por meio de outra função, permitindo que somente valores positivos sejam aceitos.
# Crie o help() da sua função:

def fat(x = 0):
    """
    :parametro x: o número enviado (x) será elevado ao quadrado (x * x)
    :return: retorna o valor de x²
        Somente números maiores ou iguais a 0 são permitidos. Caso contrário o programa irá se repetir até o valor ser validado!
    """

    x = int(input('Digite um número: '))
    while True:
        if x < 0:
            x = int(input('Envie um número maior ou igual a 0: '))
            continue
        else:
            return f'{x}² = {x * x}'
help(fat)
print(fat())
