import ast
from termcolor import colored

def ler_dados_climaticos(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    dados = []
    for linha in linhas:
        inicio_dict = linha.find("{")
        fim_dict = linha.find("}") + 1
        dict_str = linha[inicio_dict:fim_dict]
        ciclo_data = ast.literal_eval(dict_str)
        
        dados.append({
            'temperatura': ciclo_data['Temperatura'],
            'umidade': ciclo_data['Umidade'],
            'pressao': ciclo_data['Pressao']
        })
    return dados

def calcular_estatisticas(grandeza, dados):
    minimo = min(dados, key=lambda x: x[grandeza])[grandeza]
    maximo = max(dados, key=lambda x: x[grandeza])[grandeza]
    media = sum([d[grandeza] for d in dados]) / len(dados)
    return minimo, maximo, media

def main():
    dados = ler_dados_climaticos('dados_climaticos.txt')
    ciclos_por_dia = 24 * 6  # 24 horas * 6 ciclos por hora (cada ciclo de 10 minutos)
    vigesimo_dia = dados[(20-1)*ciclos_por_dia:20*ciclos_por_dia]

    grandezas = ['temperatura', 'umidade', 'pressao']
    estatisticas = {grandeza: calcular_estatisticas(grandeza, vigesimo_dia) for grandeza in grandezas}

    print(colored("Estatísticas do vigésimo dia:", 'blue', attrs=['bold', 'underline']))
    for grandeza, valores in estatisticas.items():
        print(colored(f"{grandeza.capitalize()} (min, max, média):", 'green'), colored(f"({valores[0]:.2f}, {valores[1]:.2f}, {valores[2]:.2f})", 'yellow'))
    
    print(colored(f"\nQuantidade de ciclos no vigésimo dia: {len(vigesimo_dia)}", 'cyan'))

if __name__ == "__main__":
    main()
