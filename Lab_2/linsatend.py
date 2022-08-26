# appending at end in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def push(self,ele):

        node = Node(ele)
        if(self.head==None):
            self.head=node
            self.tail=node
    
        else:

            self.tail.next = node
            self.tail=node
    

    def Print(self):

        curr = self.head
        while (curr!= None):

            print(curr.data,end=" --> ")
            curr= curr.next 

    
           





ll=LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(25)
        

ll.Print()  
ele=int((input("\nEnter number to be appended at end: ")))
def linsatend(LinkedList,ele):
        
         ll.push(ele)
         ll.Print()





linsatend(LinkedList, ele)

                      
