class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
    
    def show(lista):
        while lista is not None:
            print(lista.value)
            if lista.next is not None:
                lista = lista.next
            else:
                break
    
    # def removeKFromList(l, k):

        

no1 = ListNode(1)
no2 = ListNode(2)
no3 = ListNode(3)
no4 = ListNode(4)
no5 = ListNode(5)

no1.next = no2
no2.next = no3
no3.next = no4
no4.next = no5

lista = ListNode.removeKFromList(no1, 1)
ListNode.show(lista)