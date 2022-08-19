# Recursive version HCF

def HCF(S,L):
    
    X= max(S, L)
    Y = min(S, L)

    N=X%Y
    while(N!= 0):

        return (HCF(N,Y))
           
    return Y     

S=int(input("enter a number "))
L=int(input("enter a number "))

print("HCF is ",HCF(S,L))


  
    
    
    
