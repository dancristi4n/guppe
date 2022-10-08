"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Pythons, então TODOS os arquivos que criamos neste curso são módulos Python prontos para serem utilizados.

# Importando uma função específica do nosso módulo
from funções_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Importando todo o módulo (temos acessos a TODOS os elementos do módulo)
import funções_com_parametro as fcp

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))



