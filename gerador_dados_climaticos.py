import random

# Gera valores aleatórios para temperatura, umidade e pressão
dados_climaticos = {}
for ciclo in range(1, 145*7*30):  # 30 dias
    temperatura = round(random.uniform(20, 30), 2)
    umidade = round(random.uniform(40, 60), 2)
    pressao = round(random.uniform(1000, 1020), 2)
    dados_climaticos[ciclo] = {"Temperatura": temperatura, "Umidade": umidade, "Pressao": pressao}

# Imprime o dicionário
with open('dados_climaticos.txt', 'w') as file:
    # Imprime o dicionário no arquivo
    for ciclo, grandezas in dados_climaticos.items():
        file.write(f"Ciclo {ciclo}: {grandezas}\n")
