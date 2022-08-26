# delete end element in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def push(self,el):
        a= Node(el)
        if(ll.head==None):
            self.head = a
            self.tail = a
        else:
            self.tail.next=a
            self.tail=a

    def Print(self):
        tmp = self.head
        while(tmp!=None):
            print(tmp.data,end=" --> ")
            tmp=tmp.next

ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(25)

ll.Print()


def delatend(llist):
    tmp=llist.head
    if(tmp.next==None):
        llist.head=None

    while(tmp.next!=None):
        if(tmp.next.next==None):
            ll.tail=tmp
            tmp.next=None
            break
        tmp=tmp.next

delatend(ll)
print("\n")
ll.Print()

                      
