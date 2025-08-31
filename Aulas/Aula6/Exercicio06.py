#Crie um programa que contenha uma tupla com o nome de 10 linguagens de programação:
# Javascript, Rust, Swift, Python, Kotlin, Go, C#, Dart, Julia e Typescript. Em qual posição está a linguagem Python? Mostre na tela.

linguagens = ('JavaScript', 'Rust', 'Swift', 'Python', 'Kotlin', 'Go', 'C#', 'Dart', 'Julia', 'TypeScript')
i = 0
while linguagens[i] != 'Python':
    i+=1
print(f'Python está na {i+1}ª posição')
