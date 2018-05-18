# Wesley Rodrigues Guimarães
# CEULJI / ULBRA
# ESTRUTURA DE DADOS 1

# Lista encadeada
from no import No


class ListaEncadeada:
    inicio = None
    fim = None
    quantidade = 0

    def inserir_inicio(self, no):
        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.quantidade += 1
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no

    def mostrar(self):
        no = self.inicio
        while no is not None:
            if no.proximo:
                print(no.valor, no.proximo.valor)
            else:
                print(no.valor)
            no = no.proximo

    def inserir_qualquer_lugar(self, valor, valor_busca):
        no = self.inicio
        novo_valor = No(valor)

        while no is not None:
            if no.valor == valor_busca and no.proximo == None:
                no.proximo = novo_valor
                novo_valor.anterior = no
                self.quantidade += 1
                break
            elif no.valor == valor_busca and no.proximo is not None:
                proximo_no = no.proximo
                novo_valor.anterior = no
                no.proximo = novo_valor
                novo_valor.proximo = proximo_no
                self.quantidade += 1
                break
            elif no.valor != valor_busca and no.proximo == None:
                print("Erro")
                return "Erro"
            no = no.proximo

    def remove_numeros_impares(self):
        no = self.inicio
        while no is not None:
            if (no.valor % 2) != 0:
                no.valor = None

            no = no.proximo

    def remove_no(self, valor_busca):
        no = self.inicio

        if no.valor == valor_busca: # corrigido bug ao apagar primeiro nó
            self.inicio = no.proximo

        while no is not None:
            if no.valor == valor_busca:
                # no.valor = None  # Bug ao apagar primeiro nó
                no_anterior = no.anterior
                proximo_no = no.proximo

                if no_anterior:
                    no_anterior.proximo = no.proximo
                    if proximo_no:
                        proximo_no.anterior = no.anterior

                self.quantidade -= 1
                break

            no = no.proximo
