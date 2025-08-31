mochila = ['Machado', 'Camisa', 'Laranja', 'Abacate']
mochila.append('Ovos')
print(mochila)
print()

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']

for item in mochila:
  for letra in item:
    print(letra, end='')
  print()