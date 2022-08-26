# Done searching an element in linked linkedList

class Node:

    def __init__(self,data=None, next=None):

        self.data=data
        self.next=next

class linkedList:

    def __init__(self):

        self.head=None
        self.tail=None

    def push(self,ele):

        node = Node(ele)
        if(ll.head==None):
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
    
    def isrch(self,ele):

        curr=self.head
        i=1
        while (curr!= None):

            if(curr.data == ele):
                return i
            curr =curr.next 
            i=i+1   
        return -1
        

   



if __name__ =='__main__':

    ll=linkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(25)
    ll.push(40)

    ll.Print()
    
    print("\nPosition is : ", ll.isrch(20))


    

        
         









