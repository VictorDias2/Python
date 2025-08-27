# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e o percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto:

preco = float(input('Qual o preço do produto? '))
desconto = float(input('Qual o desconto em porcentagem? '))
total = preco - (preco*(desconto/100))
print(f'O preço do produto com desconto é de {total:0.2}')

# Site: https://colab.research.google.com/drive/1lTi0jG-ndgy-Na1SGpGLBYaqbzcMErzA#scrollTo=N6HKDXquM7F3
