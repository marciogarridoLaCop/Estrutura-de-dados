'''
1) Escreva um programa que cria uma fila vazia e insere os números de 1 a 5 nessa fila. 
Em seguida, remova os dois primeiros números da fila e exiba o conteúdo restante.​
'''
# Criando a fila e adicionando os valores
valores_numericos = Fila()
for i in range(1, 6):
    valores_numericos.enqueue(i)

# Removendo os dois primeiros valores da fila
valores_numericos.dequeue()
valores_numericos.dequeue()

# Exibindo o conteúdo restante
while not valores_numericos.is_empty():
    fila_atual = valores_numericos.dequeue()
    print(f"Fila atual: {fila_atual}")

'''
2) Escreva um programa que cria uma fila vazia e insere 10 números aleatórios nessa fila. 
Em seguida, remova todos os números pares da fila e exiba o conteúdo restante.​
'''

# Criando a fila e adicionando valores aleatórios
valores_numericos = Fila()
import random
for i in range(10):
    valores_numericos.enqueue(random.randint(1, 100))

# Removendo os números pares da fila
tamanho = valores_numericos.size()
for i in range(tamanho):
    numero_atual = valores_numericos.dequeue()
    if numero_atual % 2 != 0:
        valores_numericos.enqueue(numero_atual)

# Exibindo o conteúdo restante
while not valores_numericos.is_empty():
    fila_atual = valores_numericos.dequeue()
    print(f"Fila atual: {fila_atual}")

'''
3) Escreva um programa que cria uma fila vazia e insere os números de 1 a 10 nessa fila. 
Em seguida, exiba o elemento que está na posição 4 da fila.​
'''

# Criando a fila e adicionando os valores
valores_numericos = Fila()
for i in range(1, 11):
    valores_numericos.enqueue(i)

# Exibindo o elemento na posição 4
posicao = 4
for i in range(posicao - 1):
    valores_numericos.dequeue()
elemento = valores_numericos.dequeue()
print(f"Elemento na posição 4: 4")

'''
4) Inverter a fila (acrescentando uma nova função na classe original)
'''

# Criando a fila e adicionando os valores
valores_numericos = Fila()
for i in range(1, 6):
    valores_numericos.enqueue(i)

# Exibindo a fila original
print("Fila original:")
while not valores_numericos.is_empty():
    fila_atual = valores_numericos.dequeue()
    print(f"Fila atual: {fila_atual}")
    
# Invertendo a fila
valores_numericos.inverter()

# Exibindo a fila invertida
print("Fila invertida:")
while not valores_numericos.is_empty():
    fila_atual = valores_numericos.dequeue()
    print(f"Fila atual: {fila_atual}")

'''
5) Remover o elemento de maior valor (seja numérico ou caractere) ​
acrescentando uma nova função na classe original.
'''

# Criando a fila e adicionando os valores
valores = [7, 3, 9, 1, 4, 2, 6, 8, 5]
valores_letras = ["c", "a", "f", "d", "e", "b"]

fila_numerica = Fila()
for valor in valores:
    fila_numerica.enqueue(valor)

fila_letras = Fila()
for letra in valores_letras:
    fila_letras.enqueue(letra)

# Removendo o elemento de maior valor da fila numérica
fila_numerica.remover_maximo()
print("Fila numérica sem o elemento de maior valor:")
while not fila_numerica.is_empty():
    fila_atual = fila_numerica.dequeue()
    print(f"Fila atual: {fila_atual}")

# Removendo o elemento de maior valor da fila de letras
fila_letras.remover_maximo()
print("Fila de letras sem o elemento de maior valor:")
while not fila_letras.is_empty():
    fila_atual = fila_letras.dequeue()
    print(f"Fila atual: {fila_atual}")


'''
6) Remover o elemento de meno valor (seja numérico ou caractere) ​
acrescentando uma nova função na classe original como no exemplo anterior.
'''

 
# Criando a fila e adicionando os valores
valores = [7, 3, 9, 1, 4, 2, 6, 8, 5]
valores_letras = ["c", "a", "f", "d", "e", "b"]

fila_numerica = Fila()
for valor in valores:
    fila_numerica.enqueue(valor)

fila_letras = Fila()
for letra in valores_letras:
    fila_letras.enqueue(letra)

# Substituindo o elemento de menor valor da fila numérica
novo_valor_numerico = 10
fila_numerica.substituir_minimo(novo_valor_numerico)
print("Fila numérica com o menor valor substituído:")
while not fila_numerica.is_empty():
    fila_atual = fila_numerica.dequeue()
    print(f"Fila atual: {fila_atual}")

# Substituindo o elemento de menor valor da fila de letras
novo_valor_letra = "g"
fila_letras.substituir_minimo(novo_valor_letra)
print("Fila de letras com o menor valor substituído:")
while not fila_letras.is_empty():
    fila_atual = fila_letras.dequeue()
    print(f"Fila atual: {fila_atual}")


'''
7) Organizar a fila de forma crescente (prioridade por idade)​
acrescentando uma nova função na classe original.
'''

# Criando a fila e adicionando as pessoas
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 18)
pessoa3 = Pessoa("Pedro", 40)
pessoa4 = Pessoa("Ana", 30)
pessoa5 = Pessoa("Lucas", 22)

fila_pessoas = Fila()
fila_pessoas.enqueue(pessoa1)
fila_pessoas.enqueue(pessoa2)
fila_pessoas.enqueue(pessoa3)
fila_pessoas.enqueue(pessoa4)
fila_pessoas.enqueue(pessoa5)

# Organizando a fila em ordem crescente
fila_pessoas.organizar_crescente()

# Exibindo a fila organizada
print("Fila organizada em ordem crescente de idade:")
while not fila_pessoas.is_empty():
    pessoa_atual = fila_pessoas.dequeue()
    print(f"Nome: {pessoa_atual.nome}, Idade: {pessoa_atual.idade}")