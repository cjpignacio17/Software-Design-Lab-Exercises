class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.previous = None;  
        self.next = None;  
          
class DeleteEnd:  
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

    def deleteFromEnd(self):   
        if(self.head == None):  
            return;  
        else:  
            if(self.head != self.tail):   
                self.tail = self.tail.previous;   
                self.tail.next = None;  
                  
            else:  
                self.head = self.tail = None;  
                  
    def display(self):  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            print(current.data),  
            current = current.next;  
        print();  
         
dList = DeleteEnd();  
dList.addNode(1);  
dList.addNode(2);  
dList.addNode(3);  
dList.addNode(4);  
dList.addNode(5);  
   
print("Original List: ");  
dList.display();  
while(dList.head != None):  
    dList.deleteFromEnd();  
    
    print("Updated List: ");  
    dList.display();  