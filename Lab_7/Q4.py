# Binary Search Tree

class Node:
    def __init__(self, ele):
        self.left = None
        self.right = None
        self.ele = ele

def insert(root, ele):
    if root is None:
        return Node(ele)
    else:
        if root.ele == ele:
            return root
        elif root.ele < ele:
            root.right = insert(root.right, ele)
        else:
            root.left = insert(root.left, ele)
    return root

def minValue(root):
    current = root
 
    while(current.left is not None):
        current = current.left
 
    return current.ele 

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.ele,end=" ")
        inorder(root.right)


def delete(root, ele):
  
    if root is None:
        return root
  
    if ele < root.ele:
        root.left = delete(root.left, ele)
  
    elif(ele > root.ele):
        root.right = delete(root.right, ele)
  
    else:
  
        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp
  
        temp = minValue(root.right)
  
        root.ele = temp
  
        root.right = delete(root.right, temp)
  
    return root




root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)  
print("minimum is ",minValue(root)) 

print ("Delete 30")
root = delete(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)