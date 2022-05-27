class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (True):
        print(temp.data, end=" ")
        temp = temp.next
        if(temp == self.head):
          break
      print()
    else:
      print("The list is empty.")
                 
MyList = LinkedList()

first = Node(10)
MyList.head = first
first.next = MyList.head
second = Node(20)
first.next = second
second.next = MyList.head
third = Node(30)
second.next = third
third.next = MyList.head

MyList.PrintList()