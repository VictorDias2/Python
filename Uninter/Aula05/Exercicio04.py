# Escreva uma rotina que crie uma borda ao redor de uma palavra, para destacá-la como sendo um título.
# A rotina deve receber como parâmetro a palavra destacada. O tamanho da caixa de texto deverá ser adaptável, conforme o tamanho da palavra:
def borda(nome):
    print('+-' + '-'* len(nome) + '-*')
    print(f'| {nome} |')
    print('+-' + '-'* len(nome) + '-*')

print(borda('Ciência da Computação'))
