def manipulate_stack():
    stack = Stack()
    # Adicionando elementos
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Removendo um elemento
    print("Elemento removido:", stack.pop())
    
    # Tamanho da pilha
    print("Tamanho atual da pilha:", stack.size())
    
    # Elementos restantes na pilha
    print("Elementos na pilha:", stack.items)

# Teste da função
manipulate_stack()
