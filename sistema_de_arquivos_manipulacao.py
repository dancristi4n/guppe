"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

# Descobrindo se um arquivo ou diretório existe

# Diretório
print(os.path.exists('geek')) # True
print(os.path.exists('geek/university')) # True
print(os.path.exists('geek/university/geek3.py')) # True
print(os.path.exists('outro')) # False

# Paths absolutos
print(os.path.exists('C:/Users/Danilo Soares/Projetos/guppe/')) # True
print(os.path.exists('C:/Users/Danilo Soares/Projetos/guppe/geek/university')) # True
print(os.path.exists('C:/Users/Danilo Soares/Projetos/guppe/geek/university/geek3.py')) # True

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Criando arquivos

os.mknod('arquivo-teste4.txt')
os.mknod('c:/Users/Danilo Soares/Projetos/guppe/university.txt')

# Se vocês estiver utilizando no Mac OS, pode haver um erro de PermissionError

# No Windows dá AttributeError: module 'os' has no attribute 'mknod'

# OBS: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - unicos (um a um)

# Path relativo
os.mkdir('templates')

# Path absoluto
os.mkdir('c:/Users/Danilo Soares/templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos um FileExistsError

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (arvore de diretórios)
os.makedirs('templates/geek/university')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios

os.rename('geek2/novo2', 'geek2')

# Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomes arquivos e diretórios

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

# Arquivos
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para a lixeira. Eles somem.

# Removendo arquivos
os.remove('geek.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios
os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de diretórios
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2/outro/mais')
os.removedirs('geek2/mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para

os.remove('cesta1.txt') # Não vai para a lixeira. É deletado imediatamente.


# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

send2trash('cesta2.txt') # Vai pra lixeira. Pode ser restaurado.

send2trash('teste')

# OBS: Se o arquivo não existir, teremos OSError

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input() 


# Estamos um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente (não é verdade), o código acima não irá funcionar se você estiver utilizando o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile


arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""

