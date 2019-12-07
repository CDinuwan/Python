import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=0
def great():
    global i
    i+=1
    print("Hello",i)
    great()

great()
