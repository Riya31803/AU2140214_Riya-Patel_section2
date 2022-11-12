# PreOrder PostOrder InOrder Traversal

arr1=[]
arr=[]
arr2=[]
class  stack:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Preorder(root):

        if root==None:
            print("Root is empty")
    
        st=[]  
        st.append(root)  

        while(len(st)>0):
            curr = st.pop()
            arr1.append(curr.item)   

            if curr.right is not None:
                st.append(curr.right)

            if curr.left is not None:
                st.append(curr.left)    
        return arr1        
 
def peek(stack):
        if len(stack) > 0:
            return stack[-1]
        return None

        

def Postorder(root):

        if root==None:
            print("Root is empty")
    
        st=[]  
         

        while(True):

            while(root!=None):
                if(root.right!=None):
                    st.append(root.right)
                st.append(root)    

                root=root.left
            root=st.pop()    

            if (root.right is not None and
                peek(st) == root.right):
                st.pop() 
                st.append(root) 
                root = root.right
            
            else:
                arr.append(root.item)

                root=None 

            if(len(st)<=0):
                break         
def Inorder(root):

    curr=root
    st=[]

    while(True):

        if (curr!=None):

            st.append(curr)
            curr=curr.left
        elif(st):
            curr=st.pop()    
            arr2.append(curr.item)
            curr=curr.right
        else:

            break    


    
class StackNode :
    def __init__( self, item) :
        
        self.item = item
        self.left = None
        self.right = None
        self.next = next
        self.top = None
              


    
root = StackNode(10)
root.left=StackNode(8)
root.right=StackNode(2)
root.left.left = StackNode(3)
root.left.right = StackNode(5)
root.right.left = StackNode(2)
root.right.right = StackNode(7)

print("Preorder")
print(stack.Preorder(root))
print("\nPost order")

Postorder(root)
print(arr)

print("\nIn order")
Inorder(root)
print(arr2)
