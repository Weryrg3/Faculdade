from no import No
from lista_encadeada import ListaEncadeada
import random
primeiro = No(1)
segundo = No(2)
terceiro = No(3)


lista = ListaEncadeada()
lista.inserir_inicio(primeiro)
lista.inserir_inicio(segundo)
lista.inserir_inicio(terceiro)
lista.inserir_inicio(No(4))
lista.inserir_inicio(No(5))


# 1. Crie um algoritmo que popule dinamicamente um array com 100.000 posições.
def exe1():
    array = []
    for i in range(0, 100000):
        array += [i]
    # print(clock())
    print(array)

# 2. Crie um algoritmo que popule uma lista encadeada com 100.000 posições.
def exe2():
    lista = ListaEncadeada()
    for i in range(0, 100000):
        lista.inserir_inicio(No(i))

    lista.mostrar()

# 3. Comprare quanto tempo demorou para inserir 100.000 registros na lista encadeada X array.
# Comparando com clock quando adicionado ao inicio da lista o array se saiu melhor que a lista encadeada

# 4. Implemente um método que receba um valor e um valor de busca e:
    # - insira no próximo valor caso encontre;
    # - retorne erro se o valor não foi encontrado.
def exe4(lista):
    lista.inserir_qualquer_lugar(6, 10)
    lista.inserir_qualquer_lugar(6, 2)
    lista.mostrar()
# exe4(lista)

# 5. Crie um algoritmo que simule a entrada de x valores em uma lista. Permita o usuário escolher se deseja visualizar em:
# - Ordem crescente;
# - Ordem decrescente;    
# - Ordem de inserção.
def exe5():
    array = []
    for i in range(0, 10):
        array += [random.randint(1, 10)]
    return array
array = exe5()

def ordem_insercao(array):
    print(array)

def ordem_crescente(array):
    print(sorted(array))

def ordem_decrescente(array):
    print(sorted(array, reverse=True))
# ordem_insercao(array)
# ordem_crescente(array)
# ordem_decrescente(array)

# 6. Crie uma função que remova todos os números ímpares de uma lista encadeada.
def exe6(lista):
    lista.remove_numeros_impares()
    lista.mostrar()
# exe6(lista)

# 7. Crie uma função que receba um valor de busca e remova o nó caso encontre na lista.

def exe7(lista):
    lista.remove_no(5)
    lista.remove_no(4)
    lista.remove_no(3)
    lista.remove_no(2)
    lista.remove_no(1)
    
    lista.mostrar()

exe7(lista)

# lista.mostrar()
    