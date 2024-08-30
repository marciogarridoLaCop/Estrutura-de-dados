from stack import Stack
def remove_max_element():
    stack = Stack()
    stack.push(3)
    stack.push(1)
    stack.push(7)
    stack.push(5)
    
    max_value = max(stack.items)
    stack.items.remove(max_value)  # Remove a primeira ocorrência do maior valor
    
    return stack.items

# Teste da função
print("Pilha após remover o maior elemento:", remove_max_element())
