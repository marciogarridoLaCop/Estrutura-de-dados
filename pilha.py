# Implementação de uma pilha
"""
push - inclui elementos no início da lista
pop  - remove um item do topo da pilha (e retorna o valor desse item)
size - retorna o tamanho da pilha
first - retorna o primeiro elemento da pilha
last - retorna o último elemento da pilha

"""
# Criação da Classe
class Stack:

    # Criação do construtor
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()== 0:
            return None
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)
    
    def first(self):
        # retorna o primeiro elemento
        if self.size() != 0:
            return self.items[0]
    def last(self):
        # retorna o último elemento
        if self.size() != 0:
            return self.items[self.size()-1]
    
# Fim da Classe
