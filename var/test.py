def maior_lista(lista):
    if len(lista) == 1:
        [lista] = lista 
        return lista
    elif lista == []:
        return []
    else:
        # lista[0] # primeiro elemento  Ex: [1, 2, 3] = [1]
        # lista[1:] # resto da lista excluindo primeiro elemento Ex: [1, 2, 3] = [2, 3]
        maior = maior_lista(lista[1:])
        if maior > lista[0]:
            return maior
        else:
            return lista[0]

print(maior_lista([2, 3, 4, 1]))
