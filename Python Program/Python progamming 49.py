class A:
    def __init__(self):
        print("in A Init")
    def featurel1(self):
        print("Feature 1 Working")
    def fearurel(self):
        print("Feature 2 Working")

class B:
    def __init__(self):
        super().__init__()
    def featurel3(self):
        print("Feature 3 Working")
    def featurel4(self):
        print("Feature 4 Working")

class C(A,B):
    def __init__(self):
        print("in C init")
        
a1=C()