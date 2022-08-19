# Check weather the string is Palindrome or not

def Pali(Str,f,l):

    

    if(f==l):
        return True

    if(Str[f]!= Str[l]):
        return False

    if(f < l+1):
        return(Pali(Str, f+1, l-1))        

    return True

    
    

S=input("Enter a String:  ")
x=len(S)
print("Is string a palindrome? : ",Pali(S,0,x-1))
