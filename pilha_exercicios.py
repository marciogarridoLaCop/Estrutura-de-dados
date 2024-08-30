from pilha import Stack

def manipulate_stack():
    MinhaPilha = Stack()
    while True:
        item = input("Digite um elemento para adicionar à pilha (ou 'sair' para parar): ")
        if item.lower() == 'sair':
            break
        MinhaPilha.push(item)
    print("Todos os elementos foram adicionados.")
    print("Elementos na pilha antes de remover um:", MinhaPilha.items)
    if MinhaPilha.size() > 0:
        print("Elemento removido:", MinhaPilha.pop())
    print("Elementos na pilha após remover um:", MinhaPilha.items)

def invert_stack():
    MinhaPilha = Stack()
    n = int(input("Quantos elementos você deseja adicionar à pilha? "))
    for i in range(n):
        item = input(f"Digite o elemento {i+1}: ")
        MinhaPilha.push(item)
    print("Pilha antes de inverter:", MinhaPilha.items)
    inverted_items = []
    while MinhaPilha.size() > 0:
        inverted_items.append(MinhaPilha.pop())
    for item in inverted_items:
        MinhaPilha.push(item)
    print("Pilha após inverter:", MinhaPilha.items)

def remove_max_element():
    MinhaPilha = Stack()
    n = int(input("Quantos elementos você deseja adicionar à pilha? "))
    for i in range(n):
        item = input(f"Digite o elemento {i+1}: ")
        MinhaPilha.push(item)
    print("Pilha original:", MinhaPilha.items)
    max_value = max(MinhaPilha.items, key=lambda x: float(x) if x.isdigit() else x)
    MinhaPilha.items.remove(max_value)
    print("Pilha após remover o maior elemento:", MinhaPilha.items)

def replace_min_element():
    MinhaPilha = Stack()
    n = int(input("Quantos elementos você deseja adicionar à pilha? "))
    for i in range(n):
        item = input(f"Digite o elemento {i+1}: ")
        MinhaPilha.push(item)
    new_value = input("Digite o novo valor para substituir o menor elemento: ")
    min_value = min(MinhaPilha.items, key=lambda x: float(x) if x.isdigit() else x)
    index_min = MinhaPilha.items.index(min_value)
    MinhaPilha.items[index_min] = new_value
    print("Pilha após substituir o menor elemento:", MinhaPilha.items)

def sort_stack():
    MinhaPilha = Stack()
    n = int(input("Quantos elementos você deseja adicionar à pilha? "))
    for i in range(n):
        item = input(f"Digite o elemento {i+1}: ")
        MinhaPilha.push(item)
    print("Pilha antes de ordenar:", MinhaPilha.items)
    MinhaPilha.items.sort(key=lambda x: float(x) if x.isdigit() else x)
    print("Pilha após ordenar:", MinhaPilha.items)

# Teste das funções
if __name__ == '__main__':
    print("Testando manipulação da pilha:")
    manipulate_stack()
    print("\nTestando inversão da pilha:")
    invert_stack()
    print("\nTestando remoção do maior elemento da pilha:")
    remove_max_element()
    print("\nTestando substituição do menor elemento da pilha:")
    replace_min_element()
    print("\nTestando ordenação da pilha:")
    sort_stack()
