"""
Min e Max

max() -> Retorna o maior valor em um iterável ou maior de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) # 129

dicionario = {'f': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'a': 129}
print(max(dicionario)) # 129
print(max(dicionario.values())) # 129

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek University'))

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) # 129

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla)) # 129

dicionario = {'f': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'a': 129}
print(min(dicionario)) # 129
print(min(dicionario.values())) # 129

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University')) # o espaço ' ' é o menor valor

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # Tim

print(min(nomes)) # Arya

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))

"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar música mais tocada e a menos tocada sem usar max(), min() e lambda?

max = 0
for m in musicas:    
    if m['tocou'] > max:
        max = m['tocou']

for m in musicas:
    if m['tocou'] == max:
        print(m['titulo'])

min = 99999
for m in musicas:    
    if m['tocou'] < min:
        min = m['tocou']

for m in musicas:
    if m['tocou'] == min:
        print(m['titulo'])