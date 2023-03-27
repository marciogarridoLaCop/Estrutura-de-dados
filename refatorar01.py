while True:
    expressao = str(input('\033[33mDigite uma expressão: ')).replace(' ', '')
    erro = parentesis_esquerda = parentesis_direita = 0
    lista_operadores = ['+', '-', '/', '*', '^']
    for p in expressao:
        if p in '(':
            parentesis_esquerda += 1
        if p in ')':
            parentesis_direita += 1
    if parentesis_direita != parentesis_esquerda:
        print('\033[31mERRO1: A quantidade de parêntesis não é a mesma. FALTAM PARÊNTESIS')
        erro = 1
    for n in range(0, 10):
        if f'){n}' in expressao:
            print('\033[31mERRO2: Existe um parêntesis incorreto à esquerda de um número. FALTA OPERADOR')
            erro = 2
        if f'{n}(' in expressao:
            print('\033[31mERRO3: Existe um parêntesis incorreto à direita de um número. FALTA OPERADOR')
            erro = 3
    for o in lista_operadores:
        if f'({o}' in expressao:
            print('\033[31mERRO4: Existe um parêntesis incorreto à esquerda de um operador. FALTA NÚMERO OU INCÓGNITA')
            erro = 4
        if f'{o})' in expressao:
            print('\033[31mERRO5: Existe um parêntesis incorreto à direita de um operador. FALTA NÚMERO OU INCÓGNITA')
            erro = 5
    if expressao[-1] in lista_operadores:
        print('\033[31mERRO6: A expressão termina com operadores. FALTA NÚMERO OU INCÓGNITA')
        erro = 6
    if expressao[0] in lista_operadores:
        print('\033[31mERRO7: A expressão começa com operadores. FALTA NÚMERO OU INCÓGNITA')
        erro = 7
    if '()' in expressao:
        print('\033[31mERRO8: A expressão contém parêntesis se encostando. FALTA NÚMERO OU INCÓGNITA')
        erro = 8
    if ')(' in expressao:
        print('\033[31mERRO9: A expressão contém parêntesis se encostando. FALTA OPERADOR')
        erro = 9
    if erro == 0:
        print('\033[35mA expressão digitada está correta.')
    print(10 * '\033[34m-=-')
    continuar = str(input('\033[33mDeseja digitar uma nova expressão? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('\033[34mOBRIGADO POR UTILIZAR O PROGRAMA!')
        break
    print(10 * '\033[34m-=-')
