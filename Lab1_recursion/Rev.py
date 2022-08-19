# Printing reverse of a string

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
         
S=input("Enter a String:  ")
print("Reverse of String is : ",reverse(S))