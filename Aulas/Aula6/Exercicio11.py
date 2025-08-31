def leitor_vogais(quant, letra): #Função da leitura de quantidade de vogais
    if quant == 1:
        print(f' {quant} vogal "{letra}",', end='')
    elif quant > 1:
        print(f' {quant} vogais "{letra}",', end='')

palavras = ('Amor', 'Paz', 'Mansidão', 'Temperança', 'cd', 'ORGANIZAçÕes')
vogalA, vogalE, vogalI, vogalO, vogalU, cont = 0, 0, 0, 0, 0, 0

# Programa principal que organiza a quant de vogais em suas determinadas variáveis e confere também já com acentuação:
for palavra in palavras:
    while cont != len(palavra):
        if palavra[cont].upper() == 'A' or palavra[cont].upper()== 'Ã' or palavra[cont].upper() == 'Á:' or palavra[cont].upper() == 'Â':
            vogalA += 1
        if palavra[cont].upper() == 'E' or palavra[cont].upper() == 'É' or palavra[cont].upper() == 'Ê':
            vogalE += 1
        if palavra[cont].upper() == 'I' or palavra[cont].upper() == 'Í':
            vogalI += 1
        if palavra[cont].upper() == 'O' or palavra[cont].upper() == 'Ó' or palavra[cont].upper() == 'Ô' or palavra[cont].upper() == 'Õ':
            vogalO += 1
        if palavra[cont].upper() == 'U' or palavra[cont].upper() == 'Ú':
            vogalU += 1
        cont += 1

# Condição que executa se não houver nenhuma vogal:
    if vogalA == 0 and vogalE == 0 and vogalI == 0 and vogalO == 0 and vogalU == 0:
        print(f'"{palavra}" não existe nenhuma vogal,')
# Se houver alguma vogal cai na função:
    else:
        print(f'"{palavra}" têm', end='')
        leitor_vogais(vogalA, 'a')
        leitor_vogais(vogalE, 'e')
        leitor_vogais(vogalI, 'i')
        leitor_vogais(vogalO, 'o')
        leitor_vogais(vogalU, 'u')
        print()
    vogalA, vogalE, vogalI, vogalO, vogalU, cont = 0, 0, 0, 0, 0, 0
print('🤯🤯')
