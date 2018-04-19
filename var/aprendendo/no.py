class No:
    def __init__(self, valor):
        self.anterior = None
        self.valor = valor
        self.proximo = None

    def percorrer(node):
        print(node.valor)
        
        if node.proximo != None:
            No.percorrer(node.proximo)
    
    def inserir_inicio(node, valor):
        valor_inicial = No(valor)
        node.anterior = valor_inicial
        valor_inicial.proximo = node
        return valor_inicial
    

no1 = No(1)

# no1.proximo = no2
# no2.proximo = no3

no1 = No.inserir_inicio(no1, 2)
no1 = No.inserir_inicio(no1, 3)
# no1 = No.inserir_fim(no1, 4)
print(no1.proximo)
# No.percorrer(no1)
