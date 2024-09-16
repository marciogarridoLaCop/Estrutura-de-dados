def calcular(valores):
    min_valor = min(valores)
    max_valor = max(valores)
    media_valor = sum(valores) / len(valores)
    return min_valor, max_valor, media_valor

with open('dadosclimaticos.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

dados_ciclos = [linha.strip() for linha in linhas if 'Ciclo' in linha]

temperaturas = []
umidades = []
pressoes = []

for ciclo in dados_ciclos:
    base = ciclo.split(':', 1)[1]
    valores = eval(base)
    temperaturas.append(valores['Temperatura'])
    umidades.append(valores['Umidade'])
    pressoes.append(valores['Pressao'])

dia_20_ciclos = range(19 * 60, 20 * 60)

while True:
    print("Escolha a grandeza climática que deseja visualizar:")
    print("1. Temperatura")
    print("2. Umidade")
    print("3. Pressão")
    print("4. Sair")

    opcao = input("\n\n\nDigite o número da opção desejada: ")

    if opcao == '4':
        print("Saindo do programa.")
        break
    elif opcao in ('1', '2', '3'):
        if opcao == '1':
            valores = temperaturas
            grandeza = "Temperatura"
        elif opcao == '2':
            valores = umidades
            grandeza = "Umidade"
        elif opcao == '3':
            valores = pressoes
            grandeza = "Pressão"

        valores_escolhidos = [valores[i] for i in dia_20_ciclos if i < len(valores)]
        min_val, max_val, media_val = calcular(valores_escolhidos)

        print(f"\n\n\nValores climáticos do vigésimo dia para {grandeza}:")
        print(f"Mínima: {min_val:.2f}, Média: {media_val:.2f}, Máxima: {max_val:.2f}\n\n\n")
    else:
        print("Opção inválida. Escolha uma opção válida ou digite '4' para sair.")
    print('============================================================')
