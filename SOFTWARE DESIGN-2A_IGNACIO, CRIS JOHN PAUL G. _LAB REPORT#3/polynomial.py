class polynomial:
    def __init__(self, coeff = 0, pow = 0, nxt = None):
        self.coefficient = coeff
        self.power = pow
        self.next = nxt
def create_poly(expression):
   head = None
   for element in expression:
      if head == None:
         head = polynomial(element[0], element[1])
      else:
         temp = head
      while temp.next != None:
         temp = temp.next
         if temp.next == None:
            temp.next = polynomial(element[0], element[1])
            return head
def show_poly(head):
   temp = head
   while temp.next != None:
      print(str(temp.coefficient) + 'x^' + str(temp.power), end = ' + ')
      temp = temp.next
      if temp.next == None:
         print(str(temp.coefficient) + 'x^' + str(temp.power), end=' = 0')
def solve(poly1, poly2):
   dummy = node = polynomial()
   while poly1 and poly2:
      if poly1.power > poly2.power:
         node.next = node = poly1
         poly1 = poly1.next
      elif poly1.power < poly2.power:
         node.next = node = poly2
         poly2 = poly2.next
      else:
         coef = poly1.coefficient + poly2.coefficient
      if coef: node.next = node = polynomial(coef, poly1.power)
                
poly1 = poly1.next
poly2 = poly2.next
node.next = poly1 or poly2

return dummy.next

poly1 = create_poly([[1,1], [1,2]])
poly2 = create_poly([[2,1], [3, 0]])
poly3 = solve(poly1, poly2)
show_poly(poly3)
