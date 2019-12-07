a=10
def something():
    global a
    x=globals()['a']=15
    a=79
    print("In fun",a)
    print(x)
print("Outside",a)
print(something())