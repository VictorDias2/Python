game = {'nome':'Super Mario',
         'desenvolvedora':'Nintendo',
         'ano':1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])


for values in game.values(): #(game.values()) Apenas os valores
  print(values)

for keys in game.keys(): #(game.keys()) Apenas as chaves
  print(keys)

  for keys, values in game.items():
      print(f'{keys} = {values}') #print(game.items()) A chave e o dado
