"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outros exemplos

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Pra finalizar

letras = {letra for letra in 'Geek University'}
print(letras)

nome = 'Geek University'
letras = {letra: nome.count(letra) for letra in nome}
print(letras)