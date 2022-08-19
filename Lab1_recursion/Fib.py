#Recurssive version of Fibonacci

def Fib(N):
    if(N==1):
        return 0
    if(N==2):
        return 1
            
    num = Fib(N-1)+Fib(N-2)    
    return num

X=int(input("Enter N: "))
print("Nth term is: ",Fib(X))    