# INSERÇÃO
# A classe nó:


class No:
    # na frente da lista encadeada"""após um determinado nó """ no final da lista encadeada
    # Inicia o objeto nó
    def __init__(self, valor):
        self.valor = valor  # Atribuir dados
        self.proximo = None  # Inicializar


class ListaEncadeada:
    # inicia o objeto lista encadeada
    def __init__(self):
        self.inicio = None

    def Inserir_inicio(self, novo_valor):

        # Atribui o nó, e coloca o novo valor.
        novo_valor = No(novo_valor)

        # Faz o próximo nó como inicio
        novo_no.proximo = self.inicio

        # Move o inicio para apontar para o novo nó
        self.inicio = novo_no

    # Esta função esta definida na classe da lista encadeada, Acrescenta um novo nó no final da lista, definido dentro dda classe ListaEncadeada.
    def Inserir_final(self, novo_valor):

        # 1 PASSO CRIAR UM NOVO NÓ
        # 2 PASSO INSERIR UM VALOR
        # 3 PASSO DEFINIR PRÓXIMO COMO "None"

        novo_no = No(novo_valor)

        # 4 Passo SE A LISTA ENCADEADA ESTIVER VAZIA FAÇA O NOVO NÓ COMO INICIO

        if self.inicio is None:
            self.inicio = novo_valor
            return

        # 5 PASSO PERCORRER ATÉ O ULTIMO NÓ
        ultimo = self.inicio
        while (ultimo.proximo):
            ultimo = ultimo.proximo

        # Muda o próximo para o ultimo nó
        ultimo.next = novo_no

no1 = No(1)
no2 = No(2)
no3 = No(3)

no1.proximo = No(2)
no2.proximo = No(3)

no1 = ListaEncadeada.Inserir_inicio(5)