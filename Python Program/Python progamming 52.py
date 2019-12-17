#Method Overloading not in Python

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=a+b+c
        return s

s1=Student(45,87)

print(s1.sum(5,6,6)) 

#inheritance
#Overriding

class A:

    def show(self):
        print("in A Show")
    
class B(A):
    
    def show(self):
        print("in B Show")


a1=B()
a1.show()