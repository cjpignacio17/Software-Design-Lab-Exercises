class Node:  
    def __init__(self,data):  
      self.data = data;  
      self.next = None;  
   
class CreateList:  
    def __init__(self):  
      self.head = Node(None);  
      self.tail = Node(None);  
      self.head.next = self.tail;  
      self.tail.next = self.head;  
    def add(self,data):  
      newNode = Node(data);    
      if self.head.data is None:   
        self.head = newNode;  
        self.tail = newNode;  
        newNode.next = self.head;  
      else:   
        self.tail.next = newNode;  
        self.tail = newNode;   
        self.tail.next = self.head;   
    def display(self):  
        current = self.head;  
        if self.head is None:  
          print("List is empty");  
          return;  
        else:  
            print(current.data),  
            while(current.next != self.head):  
                current = current.next;  
                print(current.data),  
    def reverse(self, current):  
        if(current.next == self.head):  
            print(current.data),  
            return;  
        self.reverse(current.next);  
        print(current.data),  
      
class CircularLinkedList:  
    cl = CreateList();  
    cl.add(1);  
    cl.add(2);  
    cl.add(3);  
    cl.add(4);  
    cl.add(5);  
    cl.add(6);  
    print("Original List: ");  
    cl.display();  
    print("\nReversed List: ");  
    cl.reverse(cl.head);  