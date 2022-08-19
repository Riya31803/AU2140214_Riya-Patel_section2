# factorial

def fact(N):

    if(N==1):
        return 1

    else:
        return(N*fact(N-1))

a=int(input("Enter number: "))
if(a==1 or a==0):
    print("1")
elif(a<0 or a%1!=0):{
    print("Factorial not defined")
}    
else:
    print(fact(a))


