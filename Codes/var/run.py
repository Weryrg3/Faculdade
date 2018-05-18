from no import No

no1 = No(1)  # No(1, None)  # no1.valor = 1, no1.proximo = None
no2 = No(2)  # No(2, None)  # no2.valor = 2, no2.proximo = None
no3 = No(3)  # No(3, None)  # no3.valor = 3, no3.proximo = None

# print(no1)  # <no.No object at 0x7f08d4079f60> == No(1, None) ou no1.No(1, None)
# print(no1.valor) # 1 == No(1) ou no1.No(1)
# print(no1.proximo) # None == No(None) ou no1.No(None)
# print(no1.outro) # 5 == No(5) ou no1.No(5)

no1 = No.insert(no1, no2)
no1 = No.insert(no1, no3)

No.show(no1)
# No.search(no1, 1)
# print(No.search(no1, 2))
