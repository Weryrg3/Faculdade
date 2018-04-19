class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_final(self, novo_valor):
        
        novo_no = Node(novo_valor)
        if self.inicio is None:
            self.inicio = novo_no
            return
        
        ultimo = self.inicio
        while (ultimo.proximo):
            ultimo = ultimo.proximo

        ultimo.proximo = novo_no



