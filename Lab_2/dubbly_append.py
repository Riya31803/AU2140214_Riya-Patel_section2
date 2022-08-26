#appending element in doubly linked list

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
        a=Node(element)
        if(self.head==None):
            self.head=a
            self.tail=a
        else:
            c=self.tail
            self.tail.next=a
            self.tail=a
            a.prev=c

    def Print(self):
        tmp = self.head
        while(tmp!=None):
            print(tmp.data ,end="-->")
            tmp=tmp.next
llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(25)

ele=int(input("enter element to be appended: "))
def linsatend(llist,ele):
    llist.push(ele)

llist.Print()
print("\n")
linsatend(llist,ele)
llist.Print()