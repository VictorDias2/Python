
while True:
  login = input('Qual o seu nome? ')

  if login.upper() != 'MODTONY':
    continue

  senha = input('Qual a sua senha? ')
  print('   ' + '-.' * 10 + '-')
  if senha == 'MinhA.senh@':
      break
print('Acesso concedido.')
