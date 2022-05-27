class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.previous = None;  
        self.next = None;  
          
class InsertEnd:  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
           
    def addAtEnd(self, data):  
        newNode = Node(data);  
          
        if(self.head == None):  
            self.head = self.tail = newNode;  
            self.head.previous = None;   
            self.tail.next = None;  
        else:   
            self.tail.next = newNode;  
            newNode.previous = self.tail;  
            self.tail = newNode;  
            self.tail.next = None;  
              
    def display(self):  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        print("Adding a node to the end of the list: ");  
        while(current != None):  
            print(current.data),  
            current = current.next;  
              
        print();    
        
dList = InsertEnd();  
dList.addAtEnd(1);  
dList.display();  
dList.addAtEnd(2);  
dList.display();  
dList.addAtEnd(3);  
dList.display();  
dList.addAtEnd(4);  
dList.display();  
dList.addAtEnd(5);  
dList.display();  