class Node:                     
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref=None

class  doublyLinkedList:     
    def __init__(self):
        self.head = None
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
    def add_begin(self,data):
      new_node=Node(data)

      if self.head is None:
          self.head=new_node
      else:
          new_node.nref=self.head
          self.head.pref=new_node
          self.head=new_node
    def add_end(self,data):
      new_node=Node(data)
      if self.head is None:
          self.head=new_node
      else:
        n=self.head
        while n.nref is not None:
             n=n.nref
        n.nref=new_node
        new_node.pref=n
       
    def Traversal_forward(self): 
        if self.head is None:
            print("Linked list is empty!")
        else:
             n=self.head
             while n is not None:
                 print(n.data)
                 n=n.nref
    def Traversal_backward(self):
        if self.head is None:
             print("LL is empty!")
        else:
             n=self.head
             while n.nref is not None:
                 n=n.nref
             while n is not None:
                print(n.data)
                n=n.pref  
                
dl1 = doublyLinkedList()
dl1.insert_empty('Monday')
dl1.add_begin('Tuesday')
dl1.Traversal_forward()   
dl1.Traversal_backward() 



                        