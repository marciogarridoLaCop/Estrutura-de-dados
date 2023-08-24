# Função para calcular mínimos, máximos e médias
def calcular_estatisticas(valores):
    min_valor = min(valores)
    max_valor = max(valores)
    media_valor = sum(valores) / len(valores)
    return min_valor, max_valor, media_valor

# Ler os dados do arquivo
with open('dadosclimaticos.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Filtrar as linhas contendo os dados dos ciclos
dados_ciclos = [linha.strip() for linha in linhas if 'Ciclo' in linha]

# Extrair os valores de temperatura, umidade e pressão
temperaturas = []
umidades = []
pressoes = []

for ciclo in dados_ciclos:
	base = ciclo.split(':', 1)[1]
	valores = eval(base)
	temperaturas.append(valores['Temperatura'])
	umidades.append(valores['Umidade'])
	pressoes.append(valores['Pressao'])

# Calcular estatísticas do vigésimo dia (índice 19)
ciclos_vigesimo_dia = range(19 * 60, 20 * 60)  # Intervalo de ciclos para o vigésimo dia (considerando 1 ciclo a cada 10 minutos)

temperaturas_vigesimo_dia = [temperaturas[i] for i in ciclos_vigesimo_dia if i < len(temperaturas)]
umidades_vigesimo_dia = [umidades[i] for i in ciclos_vigesimo_dia if i < len(umidades)]
pressoes_vigesimo_dia = [pressoes[i] for i in ciclos_vigesimo_dia if i < len(pressoes)]
min_temp, max_temp, media_temp = calcular_estatisticas(temperaturas_vigesimo_dia)
min_umidade, max_umidade, media_umidade = calcular_estatisticas(umidades_vigesimo_dia)
min_pressao, max_pressao, media_pressao = calcular_estatisticas(pressoes_vigesimo_dia)

print(f"Valores climáticos no vigésimo dia:")
print(f"Temperatura - Mín: {min_temp}, Máx: {max_temp}, Média: {media_temp}")
print(f"Umidade - Mín: {min_umidade}, Máx: {max_umidade}, Média: {media_umidade}")
print(f"Pressão - Mín: {min_pressao}, Máx: {max_pressao}, Média: {media_pressao}")
