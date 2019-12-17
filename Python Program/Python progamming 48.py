class A:
    def featurel1(self):
        print("Feature 1 working")
    def featurel2(self):
        print("Feature 2 working")
class B(A):
    def featurel3(self):
        print("Feature 3 working")
    def featurel4(self):
        print("Feature 2 Working")

    a1=A()
    a1.featurel1()