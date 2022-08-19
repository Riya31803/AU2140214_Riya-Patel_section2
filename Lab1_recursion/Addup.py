# Recursive version for adding numbers

def AddUp(N):
    sum = N
    
    if(N==1):
        return 1
    else:
        while(N>0):
         sum = sum + AddUp(N-1)
         N=N-1
         return sum
    return sum  
    
N=int(input("Enter N: "))
if(N==0):
    print("0")
    
else:

  print(AddUp(N))
