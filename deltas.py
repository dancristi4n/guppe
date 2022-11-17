"""
Trabalhando com deltas de data e hora

data_inicial = 'dd/mm/yyyy 12:55:34.931283'
data_final = 'dd/mm/yyyy 13:34:998312'

delta = data_final - data_inicial

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2023, 3, 3, 0)

# calculando o delta
tempo_para_o_evento = aniversario - data_hoje

print(type(tempo_para_o_evento))

print(repr((tempo_para_o_evento)))

print(tempo_para_o_evento)

print(f'Faltam {tempo_para_o_evento.days} dias, '
      f'{tempo_para_o_evento.seconds // 60 // 60 } horas, '
      f'{tempo_para_o_evento.seconds // 60 } segundos...' )


"""

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
