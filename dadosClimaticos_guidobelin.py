with open('dadosclimaticos.txt', 'r') as arq:
    lin = arq.readlines()


lin_vigesimo_dia = lin[19 * 60:20 * 60]


temp_vigesimo_dia = []
umi_vigesimo_dia = []
pres_vigesimo_dia = []

for linha in lin_vigesimo_dia:
    base = linha.split(':', 1)[1]
    valores = eval(base)
    temp_vigesimo_dia.append(valores['Temperatura'])
    umi_vigesimo_dia.append(valores['Umidade'])
    pres_vigesimo_dia.append(valores['Pressao'])


min_temp = min(temp_vigesimo_dia)
max_temp = max(temp_vigesimo_dia)
media_temp = sum(temp_vigesimo_dia) / len(temp_vigesimo_dia)
min_umi = min(umi_vigesimo_dia)
max_umi = max(umi_vigesimo_dia)
media_umi = sum(umi_vigesimo_dia) / len(umi_vigesimo_dia)
min_pressao = min(pres_vigesimo_dia)
max_pressao = max(pres_vigesimo_dia)
media_pressao = sum(pres_vigesimo_dia) / len(pres_vigesimo_dia)


print(f"Valores climaticos no vigesimo dia:")
print(f"Temperatura - Min: {min_temp}, Max: {max_temp}, Media: {media_temp}")
print(f"Umidade - Min: {min_umi}, Max: {max_umi}, Media: {media_umi}")
print(f"Pressão - Min: {min_pressao}, Max: {max_pressao}, Media: {media_pressao}")
