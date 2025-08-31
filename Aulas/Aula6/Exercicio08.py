# Escreva um programa em Python que leia o nome de um aluno e três notas.
# Armazene em um dicionário o nome e a média aritmética da nota. Ainda, armazene no dicionário a situação do aluno:
#Média >= 7, aprovado;
#Média < 7 e >= 5, em exame;
#Média < 5, reprovado.

nome = (input('Nome do aluno: '))
n1 = int(input(f'Digite a 1ª nota de {nome}: '))
n2 = int(input(f'Digite a 2ª nota de {nome}: '))
n3 = int(input(f'Digite a 3ª nota de {nome}: '))
media = (n1+n2+n3) / 3

if media >= 7:
    situacao = 'Aluno aprovado!'
elif (media < 7) and (media >= 5):
    situacao = 'Aluno em exame!'
else:
    situacao = 'Aluno reprovado!'

aluno = {
    "nome": nome,
    "media": media,
    "situacao": situacao
}
print(aluno)

for chave, valor in aluno.items():
  print(f'{chave} = {valor}')
