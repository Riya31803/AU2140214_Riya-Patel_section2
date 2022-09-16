#  Riya Patel - AU2140214
# Queue using linked list

class Queue:

    def __init__(self):

        self.head=None
        self.tail=None
        self.size=0

    def enqueue(self,item):
        node = QueueNode(item)

        if(self.size==0):
            self.head=node
            self.tail=node
            self.size=self.size + 1
            
        else:
            
            self.tail.next=node
            self.tail=node
            self.size=self.size + 1

    def dequeue(self):
        node = self.head
        if(self.size==0):
            print("queue is empty")
        else:    
            
            self.head = self.head.next
            self.size -= 1
            return node.item  
         

class QueueNode (object) :
    def __init__( self, item) :
        
        self.item = item
        self.next = None     

myqueue=Queue()
print("** Queue **")
myqueue.enqueue(20)
myqueue.enqueue(30)
myqueue.enqueue(10)


print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())


