"""
Tipo string

Em Python, um dado é considerado do tipo sempre que:
- Estiver entre aspas simples -> 'um string', '234', 'a'
- Estiver entre aspas duplas -> "uma string"
- Estiver entre aspas triplas -> '''uma string'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \' Jolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

# [ 0,       1]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas duplas triplas -> """uma string"""
nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, até o último elemento e inverta
"""
print(nome[::-1])  # Inversão da String Pythônico

print(nome.replace('e', 'i'))
