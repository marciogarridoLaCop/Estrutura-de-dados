from stack import Stack
def sort_stack():
    stack = Stack()
    stack.push(3)
    stack.push(1)
    stack.push(4)
    stack.push(1)
    
    # Organizando a pilha
    stack.items.sort()
    
    return stack.items

# Teste da função
print("Pilha organizada:", sort_stack())
