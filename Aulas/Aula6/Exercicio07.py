# Escreva um algoritmo em Python que crie uma lista vazia e vá adicionando valores referentes a notas de um aluno nesta lista.
# Quando o usuário desejar parar de digitar notas (digitando um valor negativo, por exemplo), calcule a média das notas digitadas.

notas = []
cont, soma = 0, 0
while True:
    nota = float(input(f'Qual a nota do aluno? (para encerrar digite um número negativo:) '))
    if nota < 0:
        break
    else:
        notas.append(nota)
        cont +=1
        continue

for i in notas:
    soma += i
print(f'A média do aluno = {soma/cont}')
