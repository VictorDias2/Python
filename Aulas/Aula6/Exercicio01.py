mochila = ('Machado', 'Camisa', 'Bacon','Abacate')
print(mochila)
print(mochila[3])
print(mochila[:2])

for item in mochila:
    print(f'Na minha mochila tem {item}')

tam = len(mochila)
for i in range (0, tam, 1):
    print(f'Na minha mochila tem: {i}')

upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade
print(mochila_grande)
