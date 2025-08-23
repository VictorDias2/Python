def omelete():
    ovos = 6 #Variável 'local' disponível somente nesse contexto
ovos = 12
omelete()
print(ovos)

print('----------')

def vinho():
    global uvas #Torna a variável 'global' pelo restante do código
    uvas = 10
uvas = 2
vinho()
print(uvas)

print('----------')

def distancia():
    global m
    m = 4
    km()

def km():
    m = 1
    cm()

def cm():
    print(m)

m = 2
distancia()
print(m)