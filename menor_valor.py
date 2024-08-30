from stack import Stack
def replace_min_element(new_value):
    stack = Stack()
    stack.push(4)
    stack.push(2)
    stack.push(9)
    
    min_value = min(stack.items)
    # Substituindo o menor valor pelo novo valor
    index_min = stack.items.index(min_value)
    stack.items[index_min] = new_value
    
    return stack.items

# Teste da função
print("Pilha após substituir o menor elemento:", replace_min_element(10))
