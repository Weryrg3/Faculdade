try:
    lista = list(input())
    while lista:
        n = 0
        for i in range(0, len(lista)):
          if lista[i] != " ":
            if n == 0:
              lista[i] = lista[i].upper()
              n = 1
            elif n == 1:
              lista[i] = lista[i].lower()
              n = 0

        print("".join(lista))
        lista = list(input())
except EOFError:
    pass