#  Riya Patel  AU2140214
# Evaluting the postfix expression using arrays
class Stack:
 
 
 def __init__(self, capacity):
  self.top = -1
  self.capacity = capacity
  
  self.array = []
 
 def isEmpty(self):
  return True if self.top == -1 else False
 

 def peek(self):
  return self.array[-1]
 

 def pop(self):
  if not self.isEmpty():
   self.top -= 1
   return self.array.pop()
  
 

 def push(self, op):
  self.top += 1
  self.array.append(op)


 def evaluatePostfix(self, exp):
  

  for i in exp:
   

   if i.isdigit():
    self.push(i)


   else:
    val1 = self.pop()
    val2 = self.pop()
    self.push(str(eval(val2 + i + val1)))

  return int(self.pop())
    
exp = "631*+2-"
obj = Stack(len(exp))
print ("postfix evaluation: %d"%(obj.evaluatePostfix(exp)))

