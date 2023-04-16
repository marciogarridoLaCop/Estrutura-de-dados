# Implementação de uma pilha com as alterações dos exercícios propostos
"""""
enqueue - inclui elementos na fila
dequeue  - remove o elemento da fila
is_empty - retorna se a fila esta vazia
size - retorna o tamanho da fila

"""
# Criação da Classe
class Fila:
    # Criação do construtor
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def inverter(self):
        pilha = Pilha()
        while not self.is_empty():
            pilha.push(self.dequeue())
        while not pilha.is_empty():
            self.enqueue(pilha.pop())

    def remover_maximo(self):
        maximo = None
        for i in range(self.size()):
            elemento_atual = self.dequeue()
            if maximo is None or elemento_atual > maximo:
                maximo = elemento_atual
            self.enqueue(elemento_atual)
        while not self.is_empty():
            elemento_atual = self.dequeue()
            if elemento_atual != maximo:
                self.enqueue(elemento_atual)        
    
    def substituir_minimo(self, novo_valor):
        minimo = None
        for i in range(self.size()):
            elemento_atual = self.dequeue()
            if minimo is None or elemento_atual < minimo:
                minimo = elemento_atual
            self.enqueue(elemento_atual)
        while not self.is_empty():
            elemento_atual = self.dequeue()
            if elemento_atual == minimo:
                self.enqueue(novo_valor)
            else:
                self.enqueue(elemento_atual)
 
    def organizar_crescente(self):
        lista_auxiliar = []
        while not self.is_empty():
            pessoa_atual = self.dequeue()
            if len(lista_auxiliar) == 0:
                lista_auxiliar.append(pessoa_atual)
            else:
                inserido = False
                for i in range(len(lista_auxiliar)):
                    if pessoa_atual.idade < lista_auxiliar[i].idade:
                        lista_auxiliar.insert(i, pessoa_atual)
                        inserido = True
                        break
                if not inserido:
                    lista_auxiliar.append(pessoa_atual)
        for pessoa in lista_auxiliar:
            self.enqueue(pessoa)
    

# Fim da Classe