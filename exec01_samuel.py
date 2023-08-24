def transformar():
    with open('dadosclimaticos.txt', 'r', encoding='utf-8') as dados:
        linhas = dados.readlines()

    data = []
    start = 2737
    end = 2881

    for linha in linhas[start:end]:
        linha_start = linha.find("{'Temperatura'")
        linha_end = linha.find("}") + 1
        linha_completa = linha[linha_start:linha_end]
        data_ciclo = eval(linha_completa)
        data.append((data_ciclo['Temperatura'], data_ciclo['Umidade'], data_ciclo['Pressao']))

    temp = [entry[0] for entry in data]
    umidades = [entry[1] for entry in data]
    pressao = [entry[2] for entry in data]

    return temp, umidades, pressao


def printar(var, tittle):
    print(f'\nValores de {tittle}:')
    print(f'Mínimo: {min(var)}')
    print(f'Maximo: {max(var)}')
    print(f'Média: {sum(var) / len(var)}')


def main():
    result = transformar()
    temp, umidade, pressao = result
    printar(temp, 'Temperatura')
    printar(umidade, 'Umidade')
    printar(pressao, 'Pressão')


main()
