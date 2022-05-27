class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.previous = None;  
        self.next = None;  
          
class DeleteMid:   
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
        self.size = 0;  
          
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
        self.size = self.size + 1;  
          
    def deleteFromMid(self):  
        if(self.head == None):  
            return;  
        else:  
            current = self.head;  
            mid = (self.size//2) if(self.size % 2 == 0) else((self.size+1)//2);  
              
            for i in range(1, mid):  
                current = current.next;  
                  
            if(current == self.head):  
                self.head = current.next;  
            elif(current == self.tail):  
                self.tail = self.tail.previous;  
            else:  
                current.previous.next = current.next;  
                current.next.previous = current.previous;  
            current = None;  
        self.size = self.size - 1;      
      
    def display(self):  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):   
            print(current.data),  
            current = current.next;  
        print();  
         
dList = DeleteMid();  
dList.addNode(1);  
dList.addNode(2);  
dList.addNode(3);  
dList.addNode(4);  
dList.addNode(5);  
   
print("Original List: ");  
dList.display();  
while(dList.head != None):  
    dList.deleteFromMid();  
    
    print("Updated List: ")  
    dList.display();  