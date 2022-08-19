def first ():

    second()
    print("I am the First")
    
def second ():
    third()
    print("I am the Second")    

def third():
    fourth()
    print("I am the Third")

def fourth():
    print("I am the fourth")

print("**********************************************")
first()  
print("**********************************************")     