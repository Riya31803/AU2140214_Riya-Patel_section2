#  Riya Patel  AU2140214
#  application of stacks : Balancing the brackets, braces, paranthesis

class Node:
 def __init__(self, data):
  self.data = data
  self.next = None

class Stack:
 def __init__(self):
  self.head = None

 def isempty(self):
  if self.head == None:
   return True
  else:
   return False

 def push(self, data):
  if self.head == None:
   self.head = Node(data)
  else:
   newnode = Node(data)
   newnode.next = self.head
   self.head = newnode
 def pop(self):
  if self.isempty():
   return None
  else:
   poppednode = self.head
   self.head = self.head.next
   poppednode.next = None
   return poppednode.data

 def peek(self):

  if self.isempty():
   return None

  else:
   return self.head.data

 def display(self):

  iternode = self.head
  if self.isempty():
   print("Stack Underflow")

  else:
   while(iternode != None):
    print(iternode.data)
    iternode = iternode.next
   return

if __name__ == "__main__":
     MyStack = Stack()


n=[]
n=(input("Enter:"))
l=len(n)

for i in range(l):
    if(n[i]=="/"and n[i-1]=="/"):
        break
    if(n[i]=="(" or n[i]==")" or n[i]=="[" or n[i]=="]" or n[i]=="{" or n[i]=="}"):
        MyStack.push(n[i])
        if(n[i]==")" or n[i]=="}" or n[i]=="]"):
             MyStack.pop()
             MyStack.pop()
if MyStack.isempty():
   print("Balanced")
else:
    print("Not balanced!!")


 




