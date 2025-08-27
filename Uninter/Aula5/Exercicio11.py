help(print()) #'Mostrar DOCSTRING'
print('Oi!')
print('--------------------------')

        #DOCSTRING: Documentação de como funciona a função:
def soma(x = 0, y = 0, z = 0): #Cabeçalho da Função
    """
        Explicação de 'Soma':
    :param x: Não obrigatório, sendo ele = 0
    :param y: Não obrigatório, sendo ele = 0
    :param z: Não obrigatório, sendo ele = 0
    :return: Soma dos 3 valores enviados
    """
    return x + y + z

soma(1, 1, 1)
help(soma)