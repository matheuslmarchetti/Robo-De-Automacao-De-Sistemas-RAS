import pandas

data_atual = pandas.to_datetime("today").strftime("%d/%m/%Y")
print(data_atual)

mes_atual = pandas.to_datetime("today").strftime("%m")
print(mes_atual)

ano_atual = pandas.to_datetime("today").strftime("%Y")
print(ano_atual)

data_inicio_mes = pandas.Period(data_atual, freq= "M").start_time.date().strftime("%d/%m/%Y")
print(data_inicio_mes)

data_final_mes = pandas.Period(data_atual, freq= "M").end_time.date().strftime("%d/%m/%Y")
print(data_final_mes)
