class A(object): 
    
    def init (self,name): self.name = name

def __str__(self):
  
    return "Name: " + str(self.name)

class B(A): 
    
    def init(self, name, age): A.init(self, name)
    
    self.age = age

def __str__(self):
   
    return "Age: " + str(self.age) + "," + A.__str__(self)

b1=B("Baksa", 20) 
print(b1.str())