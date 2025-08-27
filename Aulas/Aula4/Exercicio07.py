vogal, cons = 0, 0
frase = input("Digite uma frase: ")

for i in range(0, len(frase), 1):
    if frase[i] == ' ':
        continue

    elif frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        vogal += 1
    else:
        cons += 1

print(f'Na palavra "{frase}" existe {vogal} vogal(is) e {cons} consoante(s)')
