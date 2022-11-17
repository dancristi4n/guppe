"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado
datetime

2022-11-03 21:49:23.184480

2022-11-03 21:54:23.184480


# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente

print(datetime.datetime.now())  # 2022-11-03 21:49:23.184480 BR 03/11/2022

# datetime.datetime(year, month, day, hour, minutes, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 22, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(year=2023, hour=22, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data
print(type(evento))

print(type('31/12/2022'))

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))


"""

import datetime


evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento))