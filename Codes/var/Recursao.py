def soma(numero1, numero2):
    return numero1 + numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def divisao(numero1, numero2):
    return numero1 / numero2

def calc():
    print(soma(1, 2)) # 3
    print(multiplicacao(2, 2)) # 4
    print(subtracao(4, 2)) # 2
    print(divisao(8, 2)) # 4.0    
    
#print(calc())

lista = [1, 2, 2, 2]
print(lista[0]) # 1
print(lista[1:]) # [2, 2, 2]

def soma2(lista):
    if lista == []:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma2(lista[1:])

print(soma2([]))
print(soma2([1]))
print(soma2([1, 2, 2, 2]))