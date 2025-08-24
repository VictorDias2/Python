# Faça uma função em lambda que recebe dois valores numéricos como parâmetro.
# Ao primeiro valor, sempre some 5. Em seguida, multiplique ambos e retorne o resultado:
soma = lambda x, y: (x+5) * y                    #soma = lambda x, y: "(x+5) * y"
x1 = int(input('Digite o 1º valor: '))       #nome var = lambda parâmetro, parâmetro: "return"
y1 = int(input('Digite o 2º valor:  '))
print(soma(x1,y1))
