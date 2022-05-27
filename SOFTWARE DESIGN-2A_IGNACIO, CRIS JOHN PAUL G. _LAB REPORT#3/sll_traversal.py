class Node:                  
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:           
    def __init__(self):
        self.head = None

    def Traversal(self):   
        n = self.head
        while n is not None:
            print (n.data)
            n = n.next

list = SinglyLinkedList()
list.head = Node("Monday")
l2 = Node("Tuesday")
l3 = Node("Wedneday")

list.head.next = l2

l2.next = l3
list.Traversal()