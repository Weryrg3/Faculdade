class No:
    valor = None
    proximo = None
    anterior = None
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

root = No(1)
n1 = No(2)
# print(root)
# print(no)

root.proximo = n1
n1.anterior = root
n3 = No(3)
n1.proximo = n3
n3.anterior = n1
n4 = No(4)
n4.proximo = root
root.anterior = n4

def mostrar(n):
    while n is not None:
        if n.anterior is None and n.proximo is not None:
            print("[", "N", "|", n.valor, "|", n.proximo, "]")
        elif n.proximo is None and n.anterior is not None:
            print("[", n.anterior, "|", n.valor, "|", "N", "]")
        elif n.proximo is None and n.anterior is None:
            print("[", "N", "|", n.valor, "|", "N", "]")
        else:
            print("[", n.anterior, "|", n.valor, "|", n.proximo, "]")
        n = n.proximo

def inserir_inicio(lista, n):
    n.proximo = lista
    lista.anterior = n
    return n

def inserir_fim(lista, n):
    l = lista
    while l is not None:
        if l.proximo is None:
            l.proximo = n
            n.anterior = l
            break
        else:
            l = l.proximo
    return lista

def remover_node(lista, valor):
     l = lista
     while l is not None:
         if l.valor == valor and l.proximo is None:
             l.anterior.proximo = None
             break
         elif l.valor == valor and l.anterior is None:
             lista = l.proximo
             lista.anterior = None
             break
         elif l.valor == valor and l.proximo is not None:
             proximo = l.proximo
             anterior = l.anterior
             anterior.proximo = l.proximo
             l.proximo.anterior = anterior
             break
         else:
             l = l.proximo
     return lista

def encontre_valor(lista, valor):
    l = lista
    while l is not None:
        if l.valor == valor:
            return True
        else:
            l = l.proximo
    return False

def ordene(lista):
    array = []
    while lista is not None:
        array.append(lista.valor)
        lista = lista.proximo
    array.sort(reverse=True) #ordena uma lista simples

    new_lista = No(array[0]) # Usado para ter uma lista pré existente
    del(array[0]) # deleta o valor adicionado para não ser adicionado novamente

    for i in array:
        new_lista = inserir_inicio(new_lista, No(i))
    return new_lista
        
print("Lista normal")
mostrar(root)
print()
print("Inserir no inicio No(9)")
lista = inserir_inicio(n4, No(9))
mostrar(lista)
print()
print("Inserir no final No(10)")
lista = inserir_fim(lista, No(10))
mostrar(lista)
print()
print("Remover node No(2)")
lista = remover_node(lista, 2)
mostrar(lista)
print()
print("Encontrar valor 1")
print(encontre_valor(lista, 1))
print()
print("Ordenar uma lista")
lista = ordene(lista)
mostrar(lista)

