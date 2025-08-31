notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# Quantos 7 tem:
cont7 = notas.count(7)
print(cont7)

# Substitua o último digito por 4:
notas[-1] = 4

# A maior nota:
print(max(notas))

# Ordenando a lista:
notas.sort()

# A média das notas:
soma = 0
for i in notas:
    soma += i
media = soma/len(notas)

        #Ou
sum(notas) / len(notas) #Soma das notas / tamanho da lista

print(notas)
