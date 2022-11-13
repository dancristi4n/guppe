"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso o módulo os.

os -> Operation System - sistema operacional
# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd()) # C:\\Users\\usr\\Projetos

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('c:\\Users')) # True
print(os.path.isabs('..')) # False

# OBS: Para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com o Windows, terá que ter cuidado ao verificar diretórios.

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (windows)

# Fazer o import
import os
import platform
import sys

# Podemos ter mais detalhes no sistema operacional
# print(os.uname())       # Só funciona em posix
print(platform.uname())   # Melhor opção
print(sys.platform)       # retorna win32 em windows

print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())
print(len(os.listdir()))

"""

import os

# Podeos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)

# print(dir(arquivos[0]))

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # é um diretório? True
print(arquivos[0].is_file()) # é um arquivo? False
print(arquivos[0].is_symlink()) # é um link simbólico? False
print(arquivos[0].name) # nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estatísticas

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim abrimos um arquivo.

scanner.close()