#  Riya Patel - AU2140214
# Double ended queue using linked list

class Queue:

    def __init__(self):

        self.F_head=None
        self.F_tail=None
        self.B_head=None
        self.B_tail=None
        self.F_size=0
        self.B_size=0

    def F_enqueue(self,F_item):
        node = QueueNode(F_item,None)

        if(self.F_size==0):
            self.F_head=node
            self.F_tail=node
            self.F_size=self.F_size + 1
            
        else:
            
            self.F_tail.F_next=node
            self.F_tail=node
            self.F_size=self.F_size + 1

    def B_enqueue(self,B_item):
        node = QueueNode(None,B_item)

        if(self.B_size==0):
            self.B_head=node
            self.B_tail=node
            self.B_size=self.B_size + 1
            
        else:
            
            self.B_tail.B_next=node
            self.B_tail=node
            self.B_size=self.B_size + 1        

    def F_dequeue(self):
        node = self.F_head
        if(self.F_size==0):
            print("queue is empty")
        else:    
            
            self.F_head = self.F_head.F_next
            self.F_size -= 1
            return node.F_item  

    def B_dequeue(self):
        node = self.B_head
        if(self.B_size==0):
            print("queue is empty")
        else:    
            
            self.B_head = self.B_head.B_next
            self.B_size -= 1
            return node.B_item         
         

class QueueNode (object) :
    def __init__(self, F_item, B_item) :
        
        self.F_item = F_item
        self.B_item = B_item
        self.F_next = None    
        self.B_next=None 

F_queue=Queue()
B_queue=Queue()

print("** Front Queue **")
F_queue.F_enqueue(20)
F_queue.F_enqueue(30)
F_queue.F_enqueue(10)


print(F_queue.F_dequeue())
print(F_queue.F_dequeue())
print(F_queue.F_dequeue())

print("** Back Queue **")

B_queue.B_enqueue(200)
B_queue.B_enqueue(300)
B_queue.B_enqueue(100)

print(B_queue.B_dequeue())
print(B_queue.B_dequeue())
print(B_queue.B_dequeue())


