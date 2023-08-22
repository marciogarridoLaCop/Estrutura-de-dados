# RODAR CÓDIGO NO TERMINAL PARA FUNCIONALIDADE DE LIMPAR TELA FUNCIONAR CORRETAMENTE


from re import findall
from os import system


def carrega():
    global leitura_formatada
    with open('dadosclimaticos.txt', 'r', encoding='utf-8') as dados:
        leitura = dados.read()
    ciclos = findall(r'Ciclo (\d+): (\{.*?})', leitura)
    leitura_formatada = []
    for ciclo_num, ciclo_dados in ciclos:
        ciclo_dados = ciclo_dados.replace("'", '"')
        dicionario = {f'Ciclo {ciclo_num}': eval(ciclo_dados)}
        leitura_formatada.append(dicionario)


def mostra(x, z, y):
    inicio = 2736
    fim = 2881
    for c in range(inicio, fim):
        x.append(leitura_formatada[c][f'Ciclo {c + 1}'][z])
    print(f'Dia 20 (Ciclos {inicio + 1} à {fim} | {fim - (inicio + 1)} ciclos)\n\n'
          f'Máxima: {max(x):.2f} {y}\n'
          f'Mínima: {min(x):.2f} {y}\n'
          f'Média: {sum(x) / len(x):.2f} {y}')
    input('\n\n\nenter para continuar...')
    system('cls')


def menu():
    system('cls')
    while True:
        print('==========================================')
        esc = input('O que Deseja visualizar? \n\n'
                    '1 - Temperatura\n'
                    '2 - Umidade\n'
                    '3 - Pressão\n'
                    '0 - Sair\n'
                    '\n- ')
        system('cls')
        carrega()
        if esc == '1':
            temperatura = []
            mostra(temperatura, 'Temperatura', 'ºC')
        elif esc == '2':
            umidade = []
            mostra(umidade, 'Umidade', 'g/m³')
        elif esc == '3':
            pressao = []
            mostra(pressao, 'Pressao', 'Pa')
        elif esc == '0':
            exit()
        else:
            print('Opção inválida')
            input('\n\n\nEnter para continuar...')
            system('cls')


menu()
