class Student:
    school='Chanuka'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def info():
        print("This is Student class")

    @classmethod
    def info(cls):
        return cls.school
    
s1=Student(34,67,89)
s2=Student(89,65,39)

print(s1.avg())
print(Student.info())
Student.info()



