#removing an element from doublly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def push(self,element):
        node=Node(element)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            c=self.tail
            self.tail.next=node
            self.tail=node
            node.prev=c

    def printlst(self):
        tmp = self.head
        while(tmp!=None):
            print(tmp.data ,end="-->")
            tmp=tmp.next
llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(25)

def dubbly_remove(llist,element):
    tmp=llist.head
    el=Node(element)
    if(tmp.prev==None and tmp.data==element):
            if(tmp.next==None):
                llist.head=None
            else:
                llist.head=tmp.next
                tmp=tmp.next

    while(tmp.next!=None):
        if(tmp.data==element):
            tmp.prev.next,tmp.next.prev=tmp.next,tmp.prev
        tmp=tmp.next

    if(tmp.data == element):
        llist.tail = tmp.prev
        tmp.prev.next = None
llist.printlst()
print("\n")
dubbly_remove(llist,20)
llist.printlst()