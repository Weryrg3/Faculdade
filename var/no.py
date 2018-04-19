class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        # self.outro = 5

    def insert(atual, proximo):
        if atual.proximo == None:
            atual.proximo = proximo
        else:
            No.insert(atual.proximo, proximo)
        return atual                

    def show(node):
        print(node.valor)
        if node.proximo != None:
            No.show(node.proximo)

    # def search(node, num):
        # if node.proximo != None:
            # No.search(node.proximo)

    # def remove(node, num):
