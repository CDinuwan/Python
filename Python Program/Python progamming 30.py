def add(a,b):#Fomal Argument 
    c=a+b
    return c

print(add(8,9))#Actual Argument

def add(c,d):
    e=c+d
    print(e)

add(d=45,c=9)

def add(c=9,d):
    e=c+d
    print(e)

#Keyword Arguments
def add(c,d):
    e=c+d
    print(e)



def sum(a,*b):
    c=0
    for i in b:
        c=c=i
print(c)
sum(5,8,5670)