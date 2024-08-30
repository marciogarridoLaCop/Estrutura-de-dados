from stack import Stack
def invert_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    # Inversão da pilha
    inverted_items = []
    while stack.size() > 0:
        inverted_items.append(stack.pop())
    
    # Recolocando itens invertidos de volta na pilha
    for item in inverted_items:
        stack.push(item)
    
    return stack.items

# Teste da função
print("Pilha invertida:", invert_stack())
