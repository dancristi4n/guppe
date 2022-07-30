"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.

# Utilizando o Counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 2: 5, 3: 5, 4: 3, 5: 3, 66: 2, 45: 1, 43: 1, 34: 1})
# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

# Utilizando o Counter

from collections import Counter

# Exemplo 3

texto = """Marvel Tales and Unusual Stories were two U.S. semi-professional science fiction magazines published by William L. Crawford, a science fiction fan who believed that the pulp magazines were too limited in what they would publish. In 1933, he distributed a flyer for Unusual Stories (cover pictured), stating that no taboos would prevent the publication of worthwhile fiction. It included a page from P. Schuyler Miller's "The Titan", unsellable to professional magazines because of its sexual content. A partial issue of Unusual Stories was distributed in early 1934, and Crawford launched Marvel Tales in May 1934. Five issues of Marvel Tales and three of Unusual Stories appeared over two years. They included Robert E. Howard's "The Garden of Fear", H. P. Lovecraft's "Celephaïs", and Clifford D. Simak's "The Creator"; the last had previously been rejected because of its religious theme. By 1936, Crawford had plans to expand his enterprise, but limited finances meant that no further issues appeared."""

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))