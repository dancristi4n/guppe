"""
1. Utilizar sempre o Hint Typing
2. Utilizar, depois de codificar, o mypy para checar. Só faz sentido se for com Hint Typing

"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento=True))

cabecalho(texto='4', alinhamento=True)
