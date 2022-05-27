class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class DeleteEnd:  
 
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
    def addNode(self, data):  
        newNode = Node(data);  
          
        if(self.head == None):  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            self.tail.next = newNode;  
            self.tail = newNode;  
              
    def deleteFromEnd(self):  

        if(self.head == None):  
            print("List is empty");  
            return;  
        else:  
            if(self.head != self.tail):  
                current = self.head;  
                while(current.next != self.tail):  
                    current = current.next;  
                self.tail = current;  
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
   
sList = DeleteEnd();  
   
sList.addNode(1);  
sList.addNode(2);  
sList.addNode(3);  
sList.addNode(4);  
   
print("Original List: ");  
sList.display();  
   
while(sList.head != None):  
    sList.deleteFromEnd();  

    print("Updated List: ");  
    sList.display();  