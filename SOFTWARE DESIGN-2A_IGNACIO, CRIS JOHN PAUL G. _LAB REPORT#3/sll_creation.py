class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class CountNodes:  

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
              
    def countNodes(self):  
        count = 0;   
        current = self.head;  
        while(current != None): 
            count = count + 1;  
            current = current.next;  
            
        return count;  
       
    def display(self):  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        print("Nodes of singly linked list: ");  
        while(current != None): 
            print(current.data),  
            current = current.next;  
       
sList = CountNodes();  
 
sList.addNode(1);  
sList.addNode(2);  
sList.addNode(3);  
sList.addNode(4);  

sList.display();  
    
print("Count of nodes present in the list: " + str(sList.countNodes()));  