class Node:

    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class InsertEnd:  

    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
    def addAtEnd(self, data):  

        newNode = Node(data);  
           
        if(self.head == None):  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            self.tail.next = newNode;  
            self.tail = newNode;  
              
    def display(self):  
 
        current = self.head;  
        
        if(self.head == None):  
            print("List is empty");  
            return;  
              
        print ("Adding nodes to the end of the list: ");  
        while(current != None):  
            print(current.data)  
            current = current.next;  
   
sList = InsertEnd();  
          
sList.addAtEnd(1);  
sList.display();  
sList.addAtEnd(2);  
sList.display();  
sList.addAtEnd(3);  
sList.display();  
sList.addAtEnd(4);  
sList.display();  