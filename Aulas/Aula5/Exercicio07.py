# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, e falso, caso contrário:

def validar(pergunta, minimo = 0, maximo = 30):
    while True:
        palavra = input(pergunta)
        tamanho = len(palavra.replace(' ', ''))
        if minimo <= tamanho <= maximo:
            return f"A palavra está dentro do parâmetro exigido, tendo ela {tamanho} letras"
        elif len(palavra) < minimo:
            print(f"Para a palavra atingir o parâmetro exigido acrecente pelo menos {minimo - tamanho} letra(s)")
        else:
            print(f"Para a palavra atingir o parâmetro exigido remova pelo menos {tamanho - maximo} letra(s)")
x = validar('Digite uma String: ', 10, 20)
