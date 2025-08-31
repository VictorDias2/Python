
cadastro = {
    "nome": [],
    "nascimento": [],
    "sexo": []
}
while True:
    nome = input('Nome: ')
    nascimento = int(input('Ano de Nascimento: '))
    sexo = input('Gênero: (M/F) ')
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        sexo = input('Apresente "M" para Masculino ou F para Feminino: ')
    continuar = input('Deseja cadastrar mais pessoas? (S/N) ')

    cadastro['nome'].append(nome)
    cadastro['nascimento'].append(nascimento)
    cadastro['sexo'].append(sexo)
    print('-' * 40)

    while continuar.upper()[0] != 'N' and continuar.upper()[0] != 'S':
        continuar = input('Valor não aceito. Deseja cadastrar mais pessoas? (S/N) ')
    if continuar.upper()[0] == 'N':
        break


print(f'Foram efetuados {len(cadastro['nome'])} cadastro(s):')

for chave, valor in cadastro.items():
  print(f'{chave} = {valor}')
