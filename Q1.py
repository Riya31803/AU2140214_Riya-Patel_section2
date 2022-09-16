#  Riya Patel - AU2140214
# satck using singly linked list
class Stack :

   
    def __init__( self ): 
        self.top = None 
        self.size = 0
 
    def isEmpty( self ): 
        return self.top is None
    
   
    def __len__( self ): 
        return self.size

    
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack" 
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item
    
    
    def push( self, item ) :
        self.top = StackNode( item, self.top ) 
        self.size =self.size+1

    def Print1(self):
        node=self.top
        while(node!=None):
            print(node.item)   
            node=node.next 

class StackNode :
    def __init__( self, item, next ) :
        
        self.item = item
        self.next = next



mystack=Stack()

 

mystack.push(10)
mystack.push(30)
mystack.push(20)
print("*** STACK Items ***")
mystack.Print1()


mystack.pop()

print("*** STACK Items After pop***")
mystack.Print1()

