segundos_para_converter = int(input('Digite a quantidade de segundos que deseja converter: '))
a = segundos_para_converter // 86400
dias_para_segundos = segundos_para_converter - (a * 86400) 
b = dias_para_segundos // 3600
segundos_para_horas = dias_para_segundos - (b * 3600)
c = segundos_para_horas // 60
d = segundos_para_horas - (c * 60)



178615
print(f'{a} dias, {b} horas, {c} minutos e {d} segundos.')