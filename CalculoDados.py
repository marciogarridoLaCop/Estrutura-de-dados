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


def mostra(x, z, y, dia):
    ciclos_dia = 6 * 24
    inicio = ciclos_dia * (dia - 1) + 1
    fim = inicio + ciclos_dia
    for c in range(inicio, fim + 1):
        x.append(leitura_formatada[c][f'Ciclo {c + 1}'][z])
    print(f'Dia 20 (Ciclos {inicio} à {fim} | {fim - inicio} ciclos)\n\n'
          f'Máxima: {max(x):.2f} {y}\n'
          f'Mínima: {min(x):.2f} {y}\n'
          f'Média: {sum(x) / len(x):.2f} {y}')
    input('\n\n\nenter para continuar...')
    system('cls')


def menu():
    while True:
        system('cls')
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
            dia = input('Escolha o dia: ')
            try:
                mostra(temperatura, 'Temperatura', 'ºC', int(dia))
            except:
                print('Valor inválido')
                input('\n\n\nEnter para continuar...')
        elif esc == '2':
            umidade = []
            dia = input('Escolha o dia: ')
            try:
                mostra(umidade, 'Umidade', 'g/m³', int(dia))
            except:
                print('Valor inválido')
                input('\n\n\nEnter para continuar...')
        elif esc == '3':
            pressao = []
            dia = input('Escolha o dia: ')
            try:
                mostra(pressao, 'Pressao', 'Pa', int(dia))
            except:
                print('Valor inválido')
                input('\n\n\nEnter para continuar...')
        elif esc == '0':
            exit()
        else:
            print('Opção inválida')
            input('\n\n\nEnter para continuar...')


menu()
