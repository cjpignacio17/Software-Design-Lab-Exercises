class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.previous = None;  
        self.next = None;  
          
class CountList:  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  

    def addNode(self, data):   
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
               
    def countNodes(self):  
        counter = 0;    
        current = self.head;  
          
        while(current != None):  
            counter = counter + 1;  
            current = current.next;  
        return counter;  
               
    def display(self):   
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        print("Nodes of doubly linked list: ");  
        while(current != None):    
            print(current.data),  
            current = current.next;  
              
dList = CountList();  
dList.addNode(1);  
dList.addNode(2);  
dList.addNode(3);  
dList.addNode(4);  
dList.addNode(5);  
    
dList.display();  
   
print("\nCount of nodes present in the list: " + str(dList.countNodes()));  