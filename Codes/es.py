class Queue:
    def enqueue(valor, lista):
        return lista + [valor]

array = []
array = Queue.enqueue(1, array)
array = Queue.enqueue(2, array)
array = Queue.enqueue(3, array)
print(array)